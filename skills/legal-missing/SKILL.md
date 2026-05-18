# Skill: /legal missing

## Purpose
Identifies protections that should be in a Canadian contract but are absent. Based on Canadian commercial best practices and statutory requirements.

## Trigger
`/legal missing <file>`

## Canadian Standard Protections Checklist

### For All Commercial Contracts
- [ ] Governing law clause (which province)
- [ ] Dispute resolution (arbitration, mediation, court — and which jurisdiction)
- [ ] Force majeure clause (especially post-COVID relevance)
- [ ] Limitation of liability cap
- [ ] Indemnification clause
- [ ] Confidentiality / NDA provisions
- [ ] Intellectual property ownership (especially important in Canada — *Copyright Act*)
- [ ] Privacy and data handling (PIPEDA / provincial PIPA compliance)
- [ ] Notice provisions (method, address, deemed receipt)
- [ ] Amendment process
- [ ] Entire agreement / integration clause
- [ ] Severability clause
- [ ] Waiver provisions

### For Employment Contracts
- [ ] Reference to provincial *Employment Standards Act* (cannot contract below minimum)
- [ ] Termination clause compliant with ESA AND common law
- [ ] Reasonable notice language (or explicit ESA-only waiver drafted correctly)
- [ ] Non-compete/non-solicitation (must be reasonable; flag if absent for senior roles)
- [ ] Intellectual property assignment
- [ ] Confidentiality
- [ ] Benefits and pension summary
- [ ] Probation period (if applicable, must comply with ESA)
- [ ] Workplace harassment policy reference (*OHSA* / provincial equivalent)

### For Technology / SaaS Contracts
- [ ] Data residency (Canadian data sovereignty — especially for government clients)
- [ ] PIPEDA / Law 25 data processing obligations
- [ ] Sub-processor disclosure
- [ ] Breach notification timeline (72 hours under PIPEDA)
- [ ] SLA / uptime guarantees
- [ ] Backup and recovery obligations
- [ ] Audit rights

### For Commercial Leases
- [ ] Rent review mechanism
- [ ] Operating costs / CAM cap
- [ ] Subletting and assignment rights
- [ ] Demolition and relocation clauses
- [ ] Right of first refusal on renewal

## Output Format

```
═══════════════════════════════════════════════════
  MISSING PROTECTIONS REPORT
  Jurisdiction: [Province]
═══════════════════════════════════════════════════

MISSING PROTECTIONS SUMMARY
  Critical Missing: [n]
  Recommended Missing: [n]
  Nice-to-Have Missing: [n]

─────────────────────────────────────────────────
CRITICAL MISSING PROTECTIONS
─────────────────────────────────────────────────

🔴 [Protection Name]
  Why It Matters: [Plain-language explanation]
  Canadian Law:   [Relevant statute or common law principle]
  Risk Without It: CAD $[X] exposure / [Legal consequence]
  Suggested Language: [Draft clause ready to insert]

─────────────────────────────────────────────────
RECOMMENDED MISSING PROTECTIONS
─────────────────────────────────────────────────

🟡 [Protection Name]
  [Description and suggested language]

─────────────────────────────────────────────────
DISCLAIMER
─────────────────────────────────────────────────
This analysis identifies common protections. Not all apply
to every contract type. Consult a Canadian lawyer.
═══════════════════════════════════════════════════
```
