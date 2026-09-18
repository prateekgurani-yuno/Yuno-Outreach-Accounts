#!/usr/bin/env python3
"""Generate 1-to-outreach/ stubs from accounts/apac-tal.csv.

Usage:
    python3 scripts/make_stubs.py --priority P1
    python3 scripts/make_stubs.py --priority P1 --industry Airlines "Event & Travel Ticketing"
    python3 scripts/make_stubs.py --company YuppTV "Great Learning"

Never overwrites an existing stub, and never recreates one for a company already sitting in
2-ready-to-outreach/, 3-outreached/ or not-icp/ — so it is safe to re-run as the queue drains.
"""
import argparse, csv, datetime, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
TAL = ROOT / "accounts" / "apac-tal.csv"
QUEUE = ROOT / "1-to-outreach"
DOWNSTREAM = ["2-ready-to-outreach", "3-outreached", "not-icp"]

# Accounts already in flight or dropped outside the pipeline folders.
SKIP = {"viu", "invideo-ai", "luno"}

# STAGE values that must never produce an outreach stub, whatever the priority says.
BLOCKED_STAGES = {"do not contact"}


def normalize(name: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", name.lower())
    return re.sub(r"-+", "-", s).strip("-")


def existing() -> set:
    seen = {p.stem for p in QUEUE.glob("*.md") if not p.stem.startswith("_")}
    for folder in DOWNSTREAM:
        seen |= {p.stem for p in (ROOT / folder).glob("*.md") if not p.stem.startswith("_")}
    return seen


def stub(row: dict, today: str) -> str:
    notes = []
    if row.get("INFO"):
        notes.append(row["INFO"].strip())
    if row.get("Payment Gateway"):
        notes.append(f"Payment gateway on file: {row['Payment Gateway']} — VERIFY, not confirmed.")
    if row.get("Payment Orchestrator"):
        notes.append(
            f"Orchestrator on file: {row['Payment Orchestrator']} — VERIFY. If confirmed, this is "
            f"a displacement motion, not greenfield. Do not open with 'you have no orchestration'."
        )
    if row.get("Operating Countries") and row["Operating Countries"].strip() not in {"", "\\"}:
        notes.append(f"Operating countries on file: {row['Operating Countries']}")
    if row.get("Est. Revenue (USD)"):
        notes.append(f"Est. revenue on file: {row['Est. Revenue (USD)']} — VERIFY.")
    if row.get("STAKEHOLDERS"):
        notes.append(f"Stakeholders: {row['STAKEHOLDERS']}")
    if row.get("ADDITIONAL COMMENTS"):
        notes.append(f"Comment: {row['ADDITIONAL COMMENTS']}")
    linkedin = row.get("Company's Linkedin", "") or ""
    if linkedin.startswith("http"):
        notes.append(f"LinkedIn: {linkedin}")

    body = "\n".join(f"- {n}" for n in notes) or "- No prior context captured."
    return (
        f"# {row['COMPANY']}\n\n"
        f"**Website:** {row.get('WEBSITE') or '—'} · **Industry:** {row.get('INDUSTRY') or '—'} · "
        f"**HQ:** {row.get('HQ Country') or '—'}\n"
        f"**Priority:** {row.get('Priority') or '—'} · **Added:** {today}\n\n"
        f"## Notes\n{body}\n\n"
        f"> Everything above comes from the target account list and is an unverified starting\n"
        f"> hypothesis. `/research` must confirm each item with a source or drop it.\n"
    )


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--priority", nargs="*", default=[])
    ap.add_argument("--industry", nargs="*", default=[])
    ap.add_argument("--company", nargs="*", default=[])
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    if not (args.priority or args.industry or args.company):
        ap.error("give at least one of --priority, --industry, --company")

    rows = list(csv.DictReader(TAL.open()))
    wanted = {normalize(c) for c in args.company}
    seen, made, skipped, blocked = existing(), 0, 0, 0
    today = datetime.date.today().isoformat()

    for row in rows:
        if not row.get("COMPANY"):
            continue
        slug = normalize(row["COMPANY"])
        # An explicit --company always matches. Otherwise --priority and --industry are
        # ANDed, so `--priority P1 --industry Airlines` means "P1 airlines", not "either".
        filtered = bool(args.priority or args.industry) and (
            (not args.priority or row.get("Priority") in args.priority)
            and (not args.industry or row.get("INDUSTRY") in args.industry)
        )
        match = slug in wanted or filtered
        if not match:
            continue
        if (row.get("STAGE") or "").strip().lower() in BLOCKED_STAGES:
            print(f"BLOCKED (STAGE={row['STAGE'].strip()}): {row['COMPANY']}")
            blocked += 1
            continue
        if slug in SKIP or slug in seen:
            skipped += 1
            continue
        path = QUEUE / f"{slug}.md"
        print(("would write " if args.dry_run else "wrote ") + str(path.relative_to(ROOT)))
        if not args.dry_run:
            path.write_text(stub(row, today))
        seen.add(slug)
        made += 1

    print(f"\n{made} stub(s) {'planned' if args.dry_run else 'created'}, {skipped} skipped "
          f"(already in the pipeline or on the skip list), {blocked} blocked on STAGE.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
