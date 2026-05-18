# Skill: /legal freelancer

## Purpose
Specialized contract review from the freelancer/independent contractor's perspective under Canadian law. Flags worker misclassification risks, payment terms, IP traps, and missing protections.

## Trigger
`/legal freelancer <file>`

## Canadian Freelancer Law Context

### Worker Classification (Critical)
The CRA uses a four-part test to determine employee vs. contractor:
1. **Control**: Who controls how/when work is done?
2. **Tools**: Who provides tools/equipment?
3. **Financial risk**: Does the contractor risk profit/loss?
4. **Integration**: Is the worker integral to the business?

Misclassification consequences:
- CRA reassessment of CPP contributions (both shares) + interest + penalties
- Employment Insurance premiums owed retroactively
- Deemed employment status → ESA rights apply
- Ontario: *Tercon Contractors Ltd. v. British Columbia* — courts look past labels to substance

### Freelancer-Specific Risks in Canadian Contracts
1. **IP assignment**: Copyright in Canada vests in the creator (Copyright Act). "Work for hire" doctrine is narrower than US law — must be explicitly assigned
2. **Payment timing**: No statutory requirement for quick payment (unlike employment) — negotiate 15-day terms
3. **HST/GST**: Ensure you can charge HST/GST on invoices
4. **Non-competes**: May be unenforceable if too broad
5. **Liability caps**: Often set to fee paid — may be insufficient
6. **Termination for convenience**: Most contracts allow this — negotiate minimum notice

## Output Format

```
═══════════════════════════════════════════════════
  FREELANCER CONTRACT REVIEW — CANADIAN EDITION
  Jurisdiction: [Province] | Perspective: Contractor
═══════════════════════════════════════════════════

SAFETY SCORE: [0–100] | Grade: [A–F]

CRITICAL FLAGS FOR CANADIAN FREELANCERS
─────────────────────────────────────────────────

🔴 MISCLASSIFICATION RISK
  [Assessment of whether this contract creates employee-like
  obligations that could trigger CRA reclassification]
  CRA Risk Level: [LOW / MEDIUM / HIGH]
  If reclassified: estimated CPP/EI liability: CAD $[X]

─────────────────────────────────────────────────
IP OWNERSHIP ANALYSIS (Copyright Act)
─────────────────────────────────────────────────
  Assignment clause found: [YES / NO]
  Moral rights waiver:     [YES / NO / NOT REQUIRED]
  
  ⚠️ Under the Copyright Act (Canada), YOU own your work by default
     unless you explicitly assign it in writing.
  
  [Assessment of IP clause — fair / one-sided / missing]
  Recommendation: [Specific fix]

─────────────────────────────────────────────────
PAYMENT TERMS ANALYSIS
─────────────────────────────────────────────────
  Payment terms:     [Net X days]
  Late payment:      [Penalty / No penalty]
  HST/GST mention:   [YES / NO]
  Expense cap:       [CAD $X / None]
  
  Canadian Freelancer Best Practice: Net 15 days; 1.5%/month interest
  on overdue amounts (Interest Act, R.S.C. 1985, c. I-15).
  
  [Assessment and recommendations]

─────────────────────────────────────────────────
NON-COMPETE / NON-SOLICITATION
─────────────────────────────────────────────────
  Non-compete found:        [YES / NO]
  Duration:                 [X months/years]
  Geographic scope:         [Description]
  Enforceability (Canada):  [LIKELY / QUESTIONABLE / LIKELY UNENFORCEABLE]
  
  Note: Canadian courts apply strict reasonableness test.
  Non-competes over 12 months / national scope are rarely enforced.

─────────────────────────────────────────────────
TERMINATION ANALYSIS
─────────────────────────────────────────────────
  Termination for convenience: [YES / NO]
  Notice period:               [X days]
  Kill fee:                    [YES / NO]
  
  [Assessment — is notice fair for project duration?]

─────────────────────────────────────────────────
LIABILITY AND INSURANCE
─────────────────────────────────────────────────
  Liability cap:    [Amount / None]
  Insurance req'd:  [Type and amount if specified]
  Indemnification:  [One-way / Mutual / Missing]
  
  [Assessment — are you adequately protected?]

─────────────────────────────────────────────────
MISSING FREELANCER PROTECTIONS
─────────────────────────────────────────────────
  □ [Missing item 1 — e.g., kill fee on early termination]
  □ [Missing item 2]
  ...

─────────────────────────────────────────────────
TOP 5 NEGOTIATION PRIORITIES
─────────────────────────────────────────────────
  1. [Most important] — CAD $[X] impact
  2. ...
  5. ...

─────────────────────────────────────────────────
BEFORE YOU SIGN — CHECKLIST
─────────────────────────────────────────────────
  □ Is your GST/HST number included in the contract or invoices?
  □ Do you have E&O (professional liability) insurance if required?
  □ Have you registered your business (sole prop / corporation) in [Province]?
  □ Are you tracking this as a self-employment income source for CRA?
  □ Have you signed an NDA or confidentiality agreement separately?

─────────────────────────────────────────────────
DISCLAIMER
─────────────────────────────────────────────────
This review is from a freelancer's perspective for informational purposes.
It does not constitute legal or tax advice. Consult a Canadian lawyer
and CPA before signing or if CRA reclassification is a concern.
═══════════════════════════════════════════════════
```
