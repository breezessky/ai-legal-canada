# Skill: /legal negotiate

## Purpose
Generate specific counter-proposals with replacement language for every unfavorable clause, grounded in Canadian commercial contract standards.

## Trigger
`/legal negotiate <file>`

## Canadian Negotiation Principles
- Courts interpret ambiguous clauses against the drafter (*contra proferentem*)
- Unconscionable clauses may be voided under provincial *Unconscionable Transactions Relief Acts*
- Good faith duty in contract performance (recognized in Canadian common law since *Bhasin v. Hrynew*, 2014 SCC 71)
- Reasonable notice requirements for termination (provincial ESA minimums are floors, not ceilings)
- Non-competes must be reasonable in scope, duration, and geography to be enforceable

## Process
1. Identify all unfavorable clauses
2. Rank by financial risk (CAD)
3. Generate specific counter-proposal language for each
4. Explain the negotiating rationale

## Output Format

```
═══════════════════════════════════════════════════
  NEGOTIATION STRATEGY REPORT
  Jurisdiction: [Province] | Currency: CAD
═══════════════════════════════════════════════════

NEGOTIATION PRIORITY RANKING
  Total negotiation value: CAD $[X] – $[Y]
  [n] clauses to counter-propose

─────────────────────────────────────────────────
COUNTER-PROPOSALS (Ranked by Priority)
─────────────────────────────────────────────────

#[N] — [CLAUSE NAME]
  Risk Level:    🔴 HIGH  |  CAD Exposure: $[X]
  
  Current Language:
    "[Problematic text]"
  
  Problem:
    [Why this is unfavorable under Canadian law]
  
  Proposed Counter-Language:
    "[Your replacement text — ready to paste into contract]"
  
  Why This Works:
    [Legal rationale — Canadian statute or case law basis]
  
  Negotiation Tip:
    [Tactical advice for the negotiation conversation]
  
  Fallback Position:
    [If they won't accept your counter, what's the minimum acceptable?]

─────────────────────────────────────────────────
CANADIAN LAW LEVERAGE POINTS
─────────────────────────────────────────────────
[Statutory rights they cannot contract out of — use these as anchors]

  • Employment minimums under [Province] ESA cannot be waived
  • Privacy obligations under PIPEDA/Law 25 are mandatory
  • Consumer protection rights under [Province] Consumer Protection Act
  • Duty of good faith: Bhasin v. Hrynew, 2014 SCC 71

─────────────────────────────────────────────────
WALK-AWAY TRIGGERS
─────────────────────────────────────────────────
[Clauses that are so one-sided you should not sign at all]

─────────────────────────────────────────────────
DISCLAIMER
─────────────────────────────────────────────────
Counter-proposals are starting points, not final legal text.
Have a Canadian lawyer review any negotiated contract.
═══════════════════════════════════════════════════
```
