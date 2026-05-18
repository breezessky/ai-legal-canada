# Skill: /legal plain

## Purpose
Translates every clause from legal jargon into plain English (or French for Quebec contracts) that any Canadian business owner can understand.

## Trigger
`/legal plain <file>`

## Process
1. Parse the contract
2. For each clause, rewrite in plain language
3. Add a "What this means for you" section
4. Flag any clause that removes rights you have under Canadian law

## Output Format

```
═══════════════════════════════════════════════════
  PLAIN LANGUAGE TRANSLATION
  [Contract Title] | Jurisdiction: [Province]
═══════════════════════════════════════════════════

[CLAUSE NAME / SECTION NUMBER]
─────────────────────────────
Original (Legal):
  "[Excerpt of original clause]"

Plain English:
  [What this actually means in plain language]

What This Means For You:
  [Practical impact on your business or rights]

🇨🇦 Canadian Law Note:
  [If this clause is unusual, unenforceable, or required
   by Canadian law — note it here]

─────────────────────────────────────────────────

[Repeat for every clause]

─────────────────────────────────────────────────
OVERALL SUMMARY
─────────────────────────────────────────────────
In plain terms, this contract says:
  [2–3 sentence plain-English summary of the whole contract]

Top 3 things to negotiate:
  1. [Most important]
  2. [Second]
  3. [Third]

─────────────────────────────────────────────────
DISCLAIMER
─────────────────────────────────────────────────
This is a plain-language explanation, not legal advice.
Consult a licensed Canadian lawyer (barrister/solicitor)
before signing any contract.
═══════════════════════════════════════════════════
```

## Quebec Bilingual Note
If the jurisdiction is Quebec, note that under the *Charter of the French Language* (Bill 96), contracts with Quebec consumers and employees must be available in French. If the contract is English-only and Quebec applies, flag this as a compliance risk.
