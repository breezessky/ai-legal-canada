# Skill: /legal compliance

## Purpose
Run a Canadian compliance gap analysis on a website or document — covering PIPEDA, CASL, Law 25 (Quebec), AODA, WCAG, Competition Act, and provincial consumer protection laws.

## Trigger
`/legal compliance <url>`

## Canadian Compliance Frameworks

### Privacy — PIPEDA / CPPA / Law 25 / PIPA
| Requirement | PIPEDA | Law 25 (QC) | BC PIPA | AB PIPA |
|-------------|--------|-------------|---------|---------|
| Privacy Policy posted | ✅ Required | ✅ Required | ✅ Required | ✅ Required |
| Privacy Officer named | ✅ Required | ✅ Required | ✅ Required | ✅ Required |
| Breach notification (regulators) | ✅ Required | ✅ 72 hours | ✅ Required | ✅ Required |
| Breach notification (individuals) | ✅ Required | ✅ Required | ✅ Required | ✅ Required |
| PIA for new projects | ❌ Recommended | ✅ Mandatory | ❌ Recommended | ❌ Recommended |
| Portability right | ❌ (CPPA pending) | ✅ Required | ❌ | ❌ |
| Right to erasure | ❌ (CPPA pending) | ✅ Required | Limited | Limited |
| Cross-border transfer PIA | ❌ | ✅ Mandatory | ❌ | ❌ |
| Cookie consent (non-essential) | Recommended | ✅ Required | Recommended | Recommended |

### CASL — Canada's Anti-Spam Legislation
- All commercial electronic messages (CEMs) require consent
- Must identify sender (name, address, contact info)
- Must include functional unsubscribe (≤ 10 business days to process)
- Implied consent expires: 2 years (business relationship), 6 months (inquiry)
- Express consent: must be obtained separately and not bundled
- Fine: up to CAD $10M per violation (organizations)

### AODA — Accessibility for Ontarians with Disabilities Act
- Applies to organizations with 1+ employees operating in Ontario
- Website accessibility: WCAG 2.0 Level AA required for large orgs (50+ employees)
- Deadline: January 1, 2021 (large orgs), January 1, 2023 (small orgs — WCAG 2.0 Level A)
- Must have documented multi-year accessibility plan
- Fine: up to CAD $100,000/day for organizations

### Competition Act — Digital Commerce
- Misleading advertising and deceptive marketing practices are prohibited
- Drip pricing (hidden fees) is prohibited
- Testimonials must be genuine
- "Regular price" claims must be verifiable
- Fine: up to CAD $10M (first offence) / 3% of global revenue

### Provincial Consumer Protection
- Automatic renewal must be disclosed prominently
- Cancellation must be as easy as sign-up (Ontario, 2023 amendment)
- Internet agreements (ON): must provide copy of agreement; 7-day cooling off if certain requirements not met
- Quebec: cooling-off period, price disclosure, prohibited contract terms

## Process
1. Fetch and scan the provided URL
2. Check for each compliance item below
3. Score each category
4. Generate prioritized remediation plan

## Compliance Audit Checklist

### Privacy (PIPEDA/Law 25)
- [ ] Privacy policy exists and is accessible
- [ ] Privacy policy is current and accurately describes data practices
- [ ] Privacy Officer named and contactable
- [ ] Cookie consent mechanism implemented
- [ ] Data collection limited to what's necessary
- [ ] Third-party service providers listed
- [ ] Data residency disclosed
- [ ] Breach notification process in place
- [ ] Rights request process documented
- [ ] Quebec PIA obligations reviewed

### CASL
- [ ] Consent mechanism before sending marketing emails
- [ ] Double opt-in implemented (best practice)
- [ ] Sender identification in all emails
- [ ] Unsubscribe link in all marketing emails
- [ ] Unsubscribe processed within 10 business days
- [ ] Implied vs. express consent tracked
- [ ] Consent records maintained

### AODA (Ontario)
- [ ] Keyboard navigation works
- [ ] Images have alt text
- [ ] Videos have captions
- [ ] Color contrast meets WCAG 2.0 Level AA
- [ ] Forms are screen-reader accessible
- [ ] Multi-year accessibility plan published
- [ ] Accessibility feedback mechanism available

### Competition Act
- [ ] No false or misleading price claims
- [ ] No deceptive "regular price" claims
- [ ] Testimonials are genuine
- [ ] Contest rules clearly disclosed
- [ ] No drip pricing (all fees disclosed upfront)

### Consumer Protection
- [ ] Return/refund policy clearly stated
- [ ] Auto-renewal terms prominently disclosed
- [ ] Cancellation mechanism as easy as sign-up
- [ ] All prices in CAD with taxes disclosed
- [ ] Terms available in French if serving Quebec

## Output Format

```
═══════════════════════════════════════════════════
  CANADIAN COMPLIANCE AUDIT REPORT
  URL: [target] | Date: [today] | Jurisdiction: [Province]
═══════════════════════════════════════════════════

OVERALL COMPLIANCE SCORE: [X]%
  🔴 Critical Issues:   [n] (potential fines)
  🟡 Medium Issues:     [n] (remediation recommended)
  🟢 Minor Issues:      [n] (best practice gaps)
  ✅ Compliant:         [n] items

─────────────────────────────────────────────────
PRIVACY COMPLIANCE (PIPEDA / Law 25 / PIPA)
─────────────────────────────────────────────────
  Score: [X]%
  [Item]: ✅ / ⚠️ / 🔴 — [Note]
  ...
  Fine Exposure: Up to CAD $[X]

─────────────────────────────────────────────────
CASL COMPLIANCE
─────────────────────────────────────────────────
  Score: [X]%
  [Item]: ✅ / ⚠️ / 🔴 — [Note]
  ...
  Fine Exposure: Up to CAD $10M per violation

─────────────────────────────────────────────────
AODA / ACCESSIBILITY
─────────────────────────────────────────────────
  Score: [X]%
  WCAG 2.0 Level: [A / AA / Non-compliant]
  ...
  Fine Exposure: Up to CAD $100,000/day

─────────────────────────────────────────────────
COMPETITION ACT
─────────────────────────────────────────────────
  Score: [X]%
  [Item]: ✅ / ⚠️ / 🔴 — [Note]

─────────────────────────────────────────────────
CONSUMER PROTECTION
─────────────────────────────────────────────────
  Score: [X]%
  [Item]: ✅ / ⚠️ / 🔴 — [Note]

─────────────────────────────────────────────────
REMEDIATION PLAN (Priority Order)
─────────────────────────────────────────────────
  1. 🔴 [CRITICAL — Fix immediately] [Estimated effort: X hours]
  2. 🔴 [CRITICAL] ...
  3. 🟡 [MEDIUM] ...
  ...

ESTIMATED REMEDIATION COST: CAD $[X]–$[Y]
POTENTIAL FINE AVOIDED:     CAD $[X]

─────────────────────────────────────────────────
DISCLAIMER
─────────────────────────────────────────────────
This audit is for informational purposes only.
Have a Canadian privacy lawyer and accessibility consultant
conduct formal compliance reviews.
═══════════════════════════════════════════════════
```
