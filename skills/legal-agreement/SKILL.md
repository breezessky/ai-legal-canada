# Skill: /legal agreement

## Purpose
Generate business agreements tailored to Canadian corporate and commercial law — including freelancer contracts, partnerships, SOWs, MSAs, shareholders agreements, and more.

## Trigger
`/legal agreement <type>`

## Supported Agreement Types

| Type | Key Canadian Law |
|------|-----------------|
| Freelancer / Independent Contractor | Worker classification (EI Act, Income Tax Act — avoid misclassification) |
| Partnership Agreement | Provincial Partnership Acts |
| Shareholders Agreement | CBCA or provincial Business Corporations Acts |
| Master Services Agreement (MSA) | Common law contract, PIPEDA |
| Statement of Work (SOW) | Common law |
| Joint Venture Agreement | Common law, Competition Act (if competitors) |
| Loan Agreement | Interest Act, provincial limitations |
| Licensing Agreement | Copyright Act, Trade-marks Act, Patent Act |
| Distribution Agreement | Competition Act (exclusive dealing provisions) |
| Commercial Lease (summary) | Provincial commercial tenancy legislation |
| Employment Offer Letter | Provincial Employment Standards Act minimums |

## Process
1. Parse the type from user input
2. Ask for: parties, jurisdiction, key terms (if not provided)
3. Generate the agreement with Canadian law annotations
4. Flag issues specific to the type

## Key Canadian Business Law References
- *Canada Business Corporations Act* (CBCA), R.S.C. 1985, c. C-44
- *Partnership Act* (each province has one)
- *Employment Standards Act* (provincial — varies)
- *Copyright Act*, R.S.C. 1985, c. C-42 — IP ownership
- *Competition Act*, R.S.C. 1985, c. C-34 — exclusivity/pricing
- *Interest Act*, R.S.C. 1985, c. I-15 — maximum interest rates
- *Limitations Act* (provincial) — limitation periods for claims

## Freelancer / Independent Contractor Contract (Example Output)

```markdown
INDEPENDENT CONTRACTOR AGREEMENT

This Agreement is made as of [DATE] between:

[CLIENT NAME], [a corporation incorporated under the laws of PROVINCE / an 
individual] with its principal place of business at [ADDRESS]
("Client")

AND

[CONTRACTOR NAME], [a corporation / sole proprietor / partnership] operating
as [OPERATING NAME], with its principal place of business at [ADDRESS]
("Contractor")

RECITALS

The Client wishes to engage the Contractor to perform certain services, and
the Contractor agrees to perform such services, on the terms set out herein.

1. SERVICES AND DELIVERABLES

The Contractor will perform the following services:
[DESCRIPTION OF SERVICES]

Deliverables: [LIST DELIVERABLES]
Timeline:     [START DATE] to [END DATE / project completion]

2. INDEPENDENT CONTRACTOR STATUS

⚠️ WORKER CLASSIFICATION NOTICE — IMPORTANT FOR CANADIAN TAX/LEGAL PURPOSES

The Contractor is an independent contractor and NOT an employee of the Client.
This Agreement does not create an employment relationship. The Contractor:

(a) Sets its own hours and work schedule;
(b) Uses its own tools and equipment (unless otherwise agreed);
(c) May perform services for other clients concurrently;
(d) Is responsible for its own income tax remittances, CPP contributions,
    and HST/GST/QST registration (if revenue exceeds $30,000/year);
(e) Is NOT entitled to Employment Insurance, vacation pay, statutory holidays,
    or other employment benefits.

Note: CRA applies the "four-in-one" test (control, ownership of tools,
chance of profit/risk of loss, integration) to determine true employment
status. If this relationship is later found to be employment, both parties
may face significant tax and EI liability.

3. COMPENSATION

(a) Fee:     CAD $[RATE] per [hour / day / project milestone]
(b) HST/GST: The Contractor will [charge / not charge] HST/GST at the
    applicable rate. [Contractor's HST/GST registration number: [NUMBER]]
(c) Invoicing: Contractor will invoice monthly / on milestone completion
(d) Payment terms: Net [15/30] days from invoice receipt
(e) Expenses: [Reimbursed with receipts / included in fee] — maximum CAD $[X]
    per month without pre-approval

4. INTELLECTUAL PROPERTY

All work product, deliverables, inventions, and materials created by the
Contractor in performing the Services ("Work Product") shall be:

[Option A — Client Owns:] assigned to and owned exclusively by the Client
upon creation. The Contractor hereby assigns all right, title, and interest
in the Work Product, including all copyright (Copyright Act, R.S.C. 1985,
c. C-42), to the Client. The Contractor waives all moral rights in the Work
Product. The Contractor will execute any further documents required to
perfect the Client's ownership.

[Option B — Contractor Retains, Licenses:] owned by the Contractor, subject
to a perpetual, non-exclusive, royalty-free licence to the Client for internal
business use only.

Pre-existing IP: The Contractor retains ownership of all pre-existing tools,
frameworks, and IP. The Contractor grants the Client a limited licence to use
pre-existing IP embedded in the deliverables for the Client's internal purposes.

5. CONFIDENTIALITY

The Contractor agrees to hold all Client confidential information in strict
confidence and to use it only for performing the Services. This obligation
survives termination for [3] years.

6. NON-SOLICITATION (if applicable)

During the term and for [12] months after termination, the Contractor will not
solicit or hire the Client's employees or contractors without written consent.

Note: Non-compete clauses for independent contractors are subject to the same
reasonableness analysis as employment — they must be reasonable in scope,
duration, and geographic area to be enforceable under Canadian common law.

7. TERM AND TERMINATION

(a) This Agreement commences on [DATE] and continues until [END DATE / 
    project completion / terminated per this Section].
(b) Either party may terminate this Agreement on [14/30] days' written notice.
(c) The Client may terminate immediately for cause (material breach, dishonesty,
    or conduct contrary to the Client's lawful policies).
(d) Upon termination, the Contractor will deliver all Work Product completed
    to date and will be paid for all work completed and accepted.

8. DISPUTE RESOLUTION AND GOVERNING LAW

This Agreement is governed by the laws of [PROVINCE] and the federal laws
of Canada applicable therein.

Disputes: The parties will attempt to resolve disputes through good-faith
negotiation, then mediation, before resorting to litigation in the courts
of [PROVINCE].

9. GENERAL

(a) Entire Agreement: This Agreement constitutes the entire agreement.
(b) Amendments: Must be in writing and signed by both parties.
(c) Severability: Invalid provisions will be severed.
(d) Electronic Signatures: Valid under provincial electronic commerce legislation.
(e) GST/HST on Legal Services: Not applicable (this is a commercial services agreement).

SIGNATURE

[CLIENT NAME]                      [CONTRACTOR NAME]
By: ____________________           By: ____________________
Name:                              Name:
Title:                             Title:
Date:                              Date:
```

## Output Instructions
- Generate the agreement type requested
- Prompt for missing fields (parties, jurisdiction, key terms)
- For shareholders agreements: ask for share structure, voting, drag-along/tag-along
- For employment offer letters: always include ESA minimum reference
- Add disclaimer: "Template only. Review with a Canadian corporate lawyer."
