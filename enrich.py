#!/usr/bin/env python3
"""Find work emails for a list of people through Yuno's Freckle email waterfall.

Input CSV columns: name, title, company, domain (extra columns are kept).
Output CSV: the input columns plus email, email_valid, email_source, failure_reason.

Usage:
  python3 enrich.py <input.csv> [output.csv]
  python3 enrich.py --check
"""
from __future__ import annotations

import csv
import json
import os
import subprocess
import sys
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor

API_BASE = "https://next-api.freckle.io"
ORG_ID = "org_3JKPKdgcp4A4k4WlrtxbNUJkH5S"
WORKFLOW_ID = "01a0a0f3-bd61-778a-bd49-9f531ea07d1a"  # Find Work Email Waterfall
KEYCHAIN_SERVICE = "freckle-enrich"
WORKERS = 5
DEADLINE_SECONDS = 180
POLL_SECONDS = 2
OUTPUT_FIELDS = ["email", "email_valid", "email_source", "failure_reason"]


def api_key() -> str:
    key = os.environ.get("FRECKLE_API_KEY", "").strip()
    if key:
        return key
    try:
        key = subprocess.run(
            ["security", "find-generic-password", "-s", KEYCHAIN_SERVICE, "-w"],
            capture_output=True, text=True, check=True,
        ).stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        key = ""
    if not key:
        sys.exit("No Freckle token found. Copy the token, then run install.sh again.")
    return key


def call(method: str, path: str, key: str, body: dict | None = None) -> dict:
    request = urllib.request.Request(
        f"{API_BASE}{path}",
        method=method,
        data=json.dumps(body).encode() if body is not None else None,
        headers={"x-api-key": key, "x-org-id": ORG_ID, "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.loads(response.read() or b"{}")


def find_email(key: str, name: str, domain: str) -> dict:
    try:
        run_id = call("POST", f"/v2/workflows/{WORKFLOW_ID}/runs", key,
                      {"inputs": {"fullName": name, "companyDomain": domain}})["runId"]
        started = time.monotonic()
        while time.monotonic() - started < DEADLINE_SECONDS:
            payload = call("GET", f"/v2/workflow-runs/{run_id}/data", key)
            state = payload.get("data") if isinstance(payload.get("data"), dict) else payload
            status = str(state.get("status") or "").lower()
            if status == "completed":
                result = (state.get("outputs") or {}).get("result") or {}
                return {
                    "email": result.get("email") or "",
                    "email_valid": "yes" if result.get("isValid") else "no",
                    "email_source": result.get("emailSource") or "",
                    "failure_reason": result.get("failureReason") or ("" if result.get("email") else "not_found"),
                }
            if status == "failed":
                return error_row("freckle_run_failed")
            time.sleep(POLL_SECONDS)
        return error_row("timeout")
    except urllib.error.HTTPError as exc:
        return error_row(f"http_{exc.code}")
    except (urllib.error.URLError, TimeoutError, KeyError, ValueError) as exc:
        return error_row(f"error: {type(exc).__name__}")


def error_row(reason: str) -> dict:
    return {"email": "", "email_valid": "no", "email_source": "", "failure_reason": reason}


def check() -> None:
    try:
        call("GET", f"/v2/workflows/{WORKFLOW_ID}", api_key())
    except urllib.error.HTTPError as exc:
        sys.exit(f"Freckle rejected the token (HTTP {exc.code}). Ask Hernán for a new one.")
    print("Freckle token OK.")


def main(argv: list[str]) -> None:
    if argv[:1] == ["--check"]:
        check()
        return
    if not argv:
        sys.exit(__doc__)
    source = argv[0]
    target = argv[1] if len(argv) > 1 else source.rsplit(".", 1)[0] + "-emails.csv"
    with open(source, newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        rows = list(reader)
        fields = list(reader.fieldnames or [])
    missing = {"name", "domain"} - set(fields)
    if missing:
        sys.exit(f"Input CSV is missing columns: {', '.join(sorted(missing))}")

    key = api_key()

    def work(row: dict) -> dict:
        name, domain = (row.get("name") or "").strip(), (row.get("domain") or "").strip().lower()
        if not name or not domain:
            return {**row, **error_row("missing name or domain")}
        return {**row, **find_email(key, name, domain)}

    with ThreadPoolExecutor(max_workers=WORKERS) as pool:
        results = []
        for index, result in enumerate(pool.map(work, rows), start=1):
            results.append(result)
            print(f"[{index}/{len(rows)}] {result.get('name')}: {result['email'] or result['failure_reason']}",
                  flush=True)

    with open(target, "w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields + [f for f in OUTPUT_FIELDS if f not in fields])
        writer.writeheader()
        writer.writerows(results)

    valid = sum(r["email_valid"] == "yes" for r in results)
    found = sum(bool(r["email"]) for r in results)
    print(f"\n{valid} valid emails, {found - valid} found but not valid, "
          f"{len(results) - found} not found, out of {len(results)}.")
    print(f"Saved: {target}")


if __name__ == "__main__":
    main(sys.argv[1:])
