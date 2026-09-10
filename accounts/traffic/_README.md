# accounts/traffic

Supplied SimilarWeb data, one file per company, named with the same normalization as the
pipeline files (`yupptv.md`, `air-new-zealand.md`).

`/research` treats a file here as the **primary** traffic source and will not re-research
it. Without one, the country profile drops to web-search estimates, which weakens the APM
gap analysis and two ICP signals.

## Format

```markdown
# {Company Name} — SimilarWeb

**Pulled:** {YYYY-MM-DD}
**Domains:** {domain1, domain2, ...}

## {domain1}
**Total visits (last full month):** {X}
**Global rank:** {N}

| Country | Traffic Share % | Est. Monthly Visits |
|---------|-----------------|---------------------|
| ... | ... | ... |
```

Paste per domain. If a company runs several, `/research` sums visits per country and
recalculates shares from the combined total — so give it raw per-domain numbers rather than
a pre-merged table.
