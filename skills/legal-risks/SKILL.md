# Skill: /legal risks

## Purpose
Deep risk analysis of a Canadian contract. Scores each clause, estimates financial exposure in CAD, and flags statutory violations.

## Trigger
`/legal risks <file>`

## Process

1. Read the contract file
2. Extract every clause and provision
3. Apply Canadian risk scoring matrix
4. Estimate CAD financial exposure for each risk

## Risk Scoring Matrix (Canadian Law)

### Category Weights
| Risk Category | Weight | Canadian Statute Trigger |
|---------------|--------|--------------------------|
| Liability caps below statutory minimums | 30% | Provincial Limitation of Liability Acts |
| Unlawful termination clauses | 25% | Canada Labour Code / provincial ESA |
| Non-compliant privacy clauses | 20% | PIPEDA / Law 25 / PIPA |
| Unenforceable non-competes | 15% | Provincial common law / ESA |
| Missing dispute resolution | 10% | Provincial arbitration / court rules |

### Risk Levels
- 🔴 **HIGH** (8–10): Exposes you to legal liability, statutory fines, or CAD $10,000+ losses
- 🟡 **MEDIUM** (4–7): Unfavorable terms that should be negotiated
- 🟢 **LOW** (1–3): Minor concerns or standard commercial terms

## Output Format

```
═══════════════════════════════════════════════════
  RISK ANALYSIS REPORT
  Jurisdiction: [Province] | Currency: CAD
═══════════════════════════════════════════════════

RISK SUMMARY
  Total Financial Exposure: CAD $[X] – $[Y]
  High Risk Clauses:   [n]
  Medium Risk Clauses: [n]
  Low Risk Clauses:    [n]

─────────────────────────────────────────────────
DETAILED RISK BREAKDOWN
─────────────────────────────────────────────────

[CLAUSE NAME]
  Risk Level:    🔴 HIGH  |  Score: [X]/10
  CAD Exposure:  $[min] – $[max]
  Why It's Risky: [Plain-language explanation]
  Canadian Law:  [Relevant statute / case law]
  Fix:           [Specific counter-proposal]

[Repeat for all clauses]

─────────────────────────────────────────────────
STATUTORY VIOLATIONS
─────────────────────────────────────────────────
[List any clauses that violate Canadian mandatory law —
these cannot be "agreed away" and are void ab initio]

  Example: A non-compete clause exceeding reasonable limits
  is void under common law (Shafron v. KRG Insurance Brokers)

─────────────────────────────────────────────────
PROVINCIAL FINE EXPOSURE
─────────────────────────────────────────────────
  PIPEDA violation fine:     Up to CAD $100,000
  CASL violation fine:       Up to CAD $10M (organization)
  Law 25 (QC) fine:          Up to CAD $25M or 4% global revenue
  ESA violation:             Varies by province (up to $100,000+)
  Competition Act:           Up to CAD $10M (first offence)

─────────────────────────────────────────────────
DISCLAIMER
─────────────────────────────────────────────────
Risk estimates are approximations for planning purposes only.
Consult a licensed Canadian lawyer for binding legal advice.
═══════════════════════════════════════════════════
```
