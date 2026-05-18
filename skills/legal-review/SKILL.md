# Skill: /legal review

## Purpose
Full contract review using 5 parallel AI agents, calibrated to Canadian federal and provincial law. Returns a Contract Safety Score, clause analysis, and prioritized recommendations in CAD context.

## Trigger
`/legal review <file>`

## Jurisdiction
Apply the jurisdiction specified at session start. Default to Ontario common law if unspecified. For Quebec, switch to Civil Code of Quebec analysis.

## Process — 5 Parallel Agents

Launch these five agents simultaneously:

### Agent 1 — Clause Analyst (Weight: 20%)
File: `~/.claude/agents/legal-clauses.md`
- Identify and categorize every clause
- Flag clauses that conflict with mandatory Canadian statutory rights
- Note Quebec language requirements (Charter of the French Language) if applicable
- Tag clauses by type: payment, IP, termination, liability, dispute resolution, privacy, confidentiality, non-compete

### Agent 2 — Risk Assessor (Weight: 25%)
File: `~/.claude/agents/legal-risks.md`
- Score each clause 1–10 for risk
- Estimate financial exposure in **CAD**
- Flag clauses that waive consumer protection rights (provincial Consumer Protection Acts)
- Identify unenforceable non-compete clauses (Ontario *Employment Standards Act*, BC *Employment Standards Act*)
- Flag mandatory employment minimums (Canada Labour Code / provincial ESA)

### Agent 3 — Compliance Checker (Weight: 20%)
File: `~/.claude/agents/legal-compliance.md`
- PIPEDA / Bill C-27 (CPPA) data handling obligations
- CASL consent requirements if electronic communications are involved
- Quebec Law 25 if Quebec jurisdiction
- AODA accessibility obligations if Ontario and public-facing
- Competition Act if any exclusivity or pricing clauses
- Consumer Protection Acts (provincial) for B2C contracts

### Agent 4 — Terms & Obligations Mapper (Weight: 15%)
File: `~/.claude/agents/legal-terms.md`
- Map all deadlines, notice periods, payment terms
- Flag statutory notice requirements (e.g., Canada Labour Code termination notice)
- Identify auto-renewal clauses (regulated in some provinces)
- Map indemnification flows

### Agent 5 — Recommendations Engine (Weight: 20%)
File: `~/.claude/agents/legal-recommendations.md`
- Generate specific counter-proposals using Canadian precedents
- Suggest standard Canadian commercial contract language
- Rank recommendations by priority (financial risk first)

---

## Output Format

```
═══════════════════════════════════════════════════
  CONTRACT SAFETY SCORE
═══════════════════════════════════════════════════
  Score: [0–100]  |  Grade: [A/B/C/D/F]
  Jurisdiction: [Province] — [Common Law / Civil Law]
  Contract Type: [Employment / Commercial / NDA / etc.]
═══════════════════════════════════════════════════

RISK DASHBOARD
  🔴 High Risk Clauses:   [n]
  🟡 Medium Risk Clauses: [n]
  🟢 Low Risk Clauses:    [n]
  ⚠️  Compliance Issues:  [n]
  🚫 Missing Protections: [n]

─────────────────────────────────────────────────
CLAUSE-BY-CLAUSE ANALYSIS
─────────────────────────────────────────────────
[For each clause:]
  Clause: [Name]
  Risk:   [🔴 HIGH / 🟡 MEDIUM / 🟢 LOW]
  Plain English: [What it actually means]
  Canadian Law Note: [Relevant statute or precedent]
  Recommendation: [Specific fix or counter-proposal]

─────────────────────────────────────────────────
CANADIAN COMPLIANCE FLAGS
─────────────────────────────────────────────────
  PIPEDA / CPPA:   [✅ Compliant / ⚠️ Issues / 🔴 Non-compliant]
  CASL:            [✅ / ⚠️ / 🔴]
  Law 25 (QC):     [✅ / ⚠️ / 🔴 / N/A]
  Employment Law:  [✅ / ⚠️ / 🔴 / N/A]
  Consumer Prot.:  [✅ / ⚠️ / 🔴 / N/A]

─────────────────────────────────────────────────
MISSING PROTECTIONS
─────────────────────────────────────────────────
[List standard Canadian commercial protections that are absent]

─────────────────────────────────────────────────
OBLIGATIONS TIMELINE
─────────────────────────────────────────────────
[Sorted by date/trigger: deadlines, notice periods, payment dates]

─────────────────────────────────────────────────
NEGOTIATION PRIORITIES
─────────────────────────────────────────────────
  1. [Most important — CAD exposure: $X]
  2. [Second priority]
  ...

─────────────────────────────────────────────────
NEXT STEPS
─────────────────────────────────────────────────
  □ [Actionable item 1]
  □ [Actionable item 2]
  ...

─────────────────────────────────────────────────
DISCLAIMER
─────────────────────────────────────────────────
This analysis is for informational purposes only and does not
constitute legal advice. Consult a licensed Canadian lawyer
(barrister/solicitor) before signing any contract.
═══════════════════════════════════════════════════
```

## Canadian Law References
- *Canada Labour Code*, R.S.C. 1985, c. L-2
- Provincial *Employment Standards Acts*
- *Personal Information Protection and Electronic Documents Act* (PIPEDA), S.C. 2000, c. 5
- *Canada's Anti-Spam Legislation* (CASL), S.C. 2010, c. 23
- Quebec *Act respecting the protection of personal information in the private sector* (Law 25)
- *Competition Act*, R.S.C. 1985, c. C-34
- *Consumer Protection Acts* (provincial)
- *Civil Code of Quebec* (for QC jurisdiction)
