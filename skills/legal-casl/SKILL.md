# Skill: /legal casl

## Purpose
Canada-specific CASL (Canada's Anti-Spam Legislation) compliance checker and remediation guide for email marketing, electronic messages, and digital outreach campaigns. This is unique to Canadian law — no US or EU equivalent covers electronic messages as comprehensively.

## Trigger
`/legal casl <description or email/campaign details>`

## CASL Overview

Canada's Anti-Spam Legislation (S.C. 2010, c. 23) came into full force July 1, 2017.

### What CASL Covers
- **Commercial Electronic Messages (CEMs)**: Any electronic message (email, SMS, instant message, social media DM) that encourages participation in a commercial activity — even in part
- **Computer programs**: Installation of software without consent (different rules)
- **Applies to**: Anyone who sends a CEM TO a Canadian, or FROM Canada

### What CASL Does NOT Cover
- Person-to-person emails (genuine, non-commercial)
- Messages to registered charities (with some limitations)
- Messages between family members
- Messages where the sender and recipient have a prior, specific business relationship that qualifies as "existing business relationship" (EBR)
- Messages sent solely in response to a request
- Messages sent to foreign countries if the message originates outside Canada (complex — get legal advice)

### CASL vs. CAN-SPAM (US) — Key Differences
| Feature | CASL (Canada) | CAN-SPAM (US) |
|---------|---------------|---------------|
| Consent model | Opt-IN required | Opt-OUT allowed |
| Implied consent | Limited (EBR only) | Much broader |
| Penalties | Up to CAD $10M/org | Up to USD $50,000/email |
| Unsubscribe deadline | 10 business days | 10 business days |
| Private right of action | Deferred | No |
| Territorial reach | Sending TO Canada | Sent FROM US |

## Consent Types

### Express Consent (Best)
- User actively checks a box, signs up, clicks "I agree"
- Does NOT expire (until withdrawn)
- Cannot be pre-checked boxes
- Must state clearly what they're consenting to
- Record: date, method, what was shown to user

### Implied Consent (Risky — Limited Shelf Life)
| Scenario | Duration |
|----------|----------|
| Existing Business Relationship (purchased in last 2 years) | 2 years |
| Inquiry / quote request (last 6 months) | 6 months |
| Conspicuously published email address (no opt-out notice) | Until withdrawn |
| Referred by someone with EBR | 2 years |

### What Must Every CEM Include
1. **Sender identification**: Full legal name of sender (person OR organization)
2. **Sender contact information**: Mailing address + one of: phone, email, or website
3. **Unsubscribe mechanism**: Clear, functional, easy to find
4. **Unsubscribe processing**: Within 10 business days

### Consent Record Requirements
For each subscriber, document:
- Date consent obtained
- Method (signup form URL, checkbox, verbal — with script)
- What the consent form said (screenshot)
- IP address (for web forms)
- Whether consent is express or implied, and the basis

## Compliance Audit

### Email / Message Review Checklist

**Consent**
- [ ] Express or valid implied consent exists for each recipient
- [ ] Consent was not obtained by pre-checked boxes
- [ ] Implied consent duration has not expired
- [ ] Consent records are maintained and accessible

**Message Content**
- [ ] Sender's full legal name is clearly identified
- [ ] Sender's mailing address is included
- [ ] Sender's email or website is included
- [ ] Message clearly identifies who is sending it (if on behalf of another)
- [ ] Unsubscribe mechanism is visible (not buried in fine print)
- [ ] Unsubscribe link is functional (not broken)
- [ ] No deceptive subject lines or sender names

**Process**
- [ ] Unsubscribes are processed within 10 business days
- [ ] Unsubscribed list is suppressed from future sends
- [ ] Consent re-confirmation before implied consent expires
- [ ] List cleaning conducted regularly

**Affiliate / Third-Party Sends**
- [ ] Third parties sending on your behalf are CASL-compliant
- [ ] Written agreements require compliance
- [ ] You are responsible for third-party violations if you "authorize" the send

## Output Format

```
═══════════════════════════════════════════════════
  CASL COMPLIANCE REPORT
  Canada's Anti-Spam Legislation (S.C. 2010, c. 23)
═══════════════════════════════════════════════════

CASL COMPLIANCE SCORE: [X]%
  🔴 Violations (potential fines):  [n]
  🟡 Gaps (remediation needed):     [n]
  ✅ Compliant:                     [n]

ESTIMATED FINE EXPOSURE:
  Per-violation fine: Up to CAD $1M (individual) / $10M (organization)
  Estimated exposure: CAD $[X] (based on estimated send volume)

─────────────────────────────────────────────────
CONSENT ANALYSIS
─────────────────────────────────────────────────
  Consent type used:        [Express / Implied / Mixed / Unknown]
  Express consent records:  [Maintained / Not maintained / Unknown]
  Implied consent tracking: [Yes / No / Partial]
  
  [Detailed assessment and risks]

─────────────────────────────────────────────────
MESSAGE CONTENT COMPLIANCE
─────────────────────────────────────────────────
  Sender identification:   ✅ / ⚠️ / 🔴
  Mailing address:         ✅ / ⚠️ / 🔴
  Contact info:            ✅ / ⚠️ / 🔴
  Unsubscribe mechanism:   ✅ / ⚠️ / 🔴
  Processing within 10 BD: ✅ / ⚠️ / 🔴

─────────────────────────────────────────────────
LIST HYGIENE REVIEW
─────────────────────────────────────────────────
  [Assessment of subscriber list quality and consent basis]

─────────────────────────────────────────────────
REMEDIATION PLAN
─────────────────────────────────────────────────
  1. 🔴 [IMMEDIATE] Re-permission campaign for un-consented contacts
  2. 🔴 [IMMEDIATE] Add sender ID and address to all templates
  3. 🟡 [WITHIN 30 DAYS] Implement consent recording system
  4. 🟡 [WITHIN 60 DAYS] Audit and purge expired implied consents
  ...

─────────────────────────────────────────────────
COMPLIANT EMAIL FOOTER TEMPLATE
─────────────────────────────────────────────────
Add this to ALL commercial emails:

---
This email was sent by [FULL LEGAL COMPANY NAME]
[MAILING ADDRESS, CITY, PROVINCE, POSTAL CODE]
[EMAIL] | [WEBSITE]

You received this email because [reason — e.g., you signed up at our website
on [DATE] / you are an existing customer].

To unsubscribe from future emails, click here: [UNSUBSCRIBE LINK]
Unsubscribe requests are processed within 10 business days.
---

─────────────────────────────────────────────────
CRTC COMPLAINT / INVESTIGATION NOTES
─────────────────────────────────────────────────
CASL is enforced by the CRTC (spam), OPC (privacy), and Competition Bureau
(false/misleading content). To report spam: https://fightspam.gc.ca

─────────────────────────────────────────────────
DISCLAIMER
─────────────────────────────────────────────────
This analysis is for informational purposes only.
CASL compliance is complex — consult a Canadian communications lawyer
for formal compliance review, especially for large send volumes.
═══════════════════════════════════════════════════
```
