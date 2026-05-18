# Skill: /legal nda

## Purpose
Generate a custom Non-Disclosure Agreement calibrated to Canadian law. Supports mutual, one-way, employee, vendor, and Quebec civil law variants.

## Trigger
`/legal nda <description>`

## NDA Types
- **Mutual**: Both parties share confidential information
- **One-way (Unilateral)**: Only one party discloses
- **Employee NDA**: Governed by provincial Employment Standards Act
- **Vendor / Supplier NDA**: Commercial context
- **Technology / IP NDA**: Includes copyright and trade secret provisions
- **Quebec NDA**: Civil Code of Quebec (art. 2803 ff.) — French version option

## Input Parsing
Extract from the user's description:
- Type (mutual / one-way / employee / vendor)
- Parties (names, roles, if provided)
- Province / jurisdiction
- Industry (affects what counts as confidential)
- Duration requested
- Purpose (e.g., "evaluating a potential acquisition", "software development project")

## Canadian Legal Requirements
- Trade secrets protected under common law (*Lac Minerals Ltd. v. International Corona Resources Ltd.*, [1989] 2 SCR 574)
- No separate trade secrets statute federally (unlike US Defend Trade Secrets Act) — rely on contract
- Non-disclosure survives employment termination but must be reasonable
- Quebec: must comply with *Civil Code of Quebec* and be available in French (Bill 96)
- Employee NDAs cannot override *Employment Standards Act* protections
- Confidentiality provisions in employment: *Rui v. Pfizer Canada*, 2010 ONCA 560

## Generated NDA Template

```markdown
NON-DISCLOSURE AGREEMENT
[MUTUAL / ONE-WAY]

This Non-Disclosure Agreement ("Agreement") is entered into as of [DATE]
between:

[DISCLOSING PARTY]: [Full legal name], a [corporation/sole proprietor/partnership]
incorporated/operating under the laws of [Province/Canada]
("Disclosing Party" / "[Short Name A]")

AND

[RECEIVING PARTY]: [Full legal name], a [corporation/sole proprietor/partnership]
incorporated/operating under the laws of [Province/Canada]
("Receiving Party" / "[Short Name B]")

(collectively, the "Parties")

RECITALS

WHEREAS the Parties wish to explore [PURPOSE] (the "Purpose") and may
exchange certain confidential information in connection therewith;

NOW THEREFORE, in consideration of the mutual covenants and agreements
contained herein and for other good and valuable consideration (the receipt
and sufficiency of which are hereby acknowledged), the Parties agree as follows:

1. DEFINITION OF CONFIDENTIAL INFORMATION

"Confidential Information" means any and all non-public information, whether
oral, written, electronic, or in any other form, disclosed by a Party
("Disclosing Party") to the other Party ("Receiving Party"), including but
not limited to: business plans, financial data, customer lists, technical
specifications, trade secrets, pricing information, intellectual property,
software code, marketing strategies, and any other information designated
as confidential or that a reasonable person would understand to be confidential
given the nature of the information and circumstances of disclosure.

Confidential Information does NOT include information that:
(a) Is or becomes publicly available through no breach of this Agreement;
(b) Was known to the Receiving Party prior to disclosure, as evidenced by
    written records predating such disclosure;
(c) Is independently developed by the Receiving Party without use of or
    reference to Confidential Information;
(d) Is rightfully received from a third party without restriction; or
(e) Is required to be disclosed by law, court order, or regulatory authority
    — provided that the Receiving Party gives prompt written notice to the
    Disclosing Party and cooperates in seeking a protective order.

2. OBLIGATIONS OF RECEIVING PARTY

The Receiving Party agrees to:
(a) Hold all Confidential Information in strict confidence;
(b) Use Confidential Information solely for the Purpose;
(c) Not disclose Confidential Information to any third party without prior
    written consent of the Disclosing Party, except to employees, contractors,
    or advisors who: (i) have a need to know for the Purpose; and (ii) are
    bound by written obligations of confidentiality no less protective than
    this Agreement;
(d) Protect Confidential Information with at least the same degree of care
    used to protect its own confidential information, but no less than
    reasonable care; and
(e) Promptly notify the Disclosing Party upon becoming aware of any actual
    or suspected unauthorized disclosure.

3. [FOR MUTUAL NDA — add reciprocal obligations mirroring Section 2]

4. INTELLECTUAL PROPERTY

Nothing in this Agreement grants any licence, right, or interest in any
Confidential Information or intellectual property of either Party. All
Confidential Information remains the exclusive property of the Disclosing Party.

Under the Copyright Act, R.S.C. 1985, c. C-42, any work created using
Confidential Information remains the property of the Disclosing Party unless
otherwise agreed in writing.

5. TERM AND TERMINATION

This Agreement commences on the date first written above and continues for
[DURATION] years, unless earlier terminated by either Party upon [30/60/90]
days' written notice.

The obligation to protect Confidential Information survives termination of
this Agreement for a period of [2/3/5] years.

6. RETURN OR DESTRUCTION OF INFORMATION

Upon written request or termination of this Agreement, the Receiving Party
shall promptly return or destroy all Confidential Information (including
all copies, notes, and summaries) and certify in writing that it has done so.

7. REMEDIES

The Parties acknowledge that any breach of this Agreement may cause
irreparable harm for which monetary damages would be inadequate. The
Disclosing Party is entitled to seek injunctive relief and other equitable
remedies without the requirement to post a bond, in addition to all other
remedies available at law or in equity.

8. GOVERNING LAW AND DISPUTE RESOLUTION

This Agreement shall be governed by and construed in accordance with the
laws of the Province of [PROVINCE] and the federal laws of Canada applicable
therein, without regard to conflict of law principles.

Any dispute arising from or relating to this Agreement shall first be
subject to good-faith negotiation for [30] days. If unresolved, the parties
shall submit to [mediation / binding arbitration under [Province] Arbitration
Act / the courts of [Province]].

9. GENERAL PROVISIONS

(a) Entire Agreement: This Agreement constitutes the entire agreement between
    the Parties regarding its subject matter and supersedes all prior
    discussions, understandings, and agreements.
(b) Amendments: No amendment to this Agreement is effective unless in writing
    and signed by both Parties.
(c) Severability: If any provision of this Agreement is found invalid or
    unenforceable, it shall be severed and the remaining provisions shall
    continue in full force.
(d) Waiver: No waiver of any provision shall be effective unless in writing.
(e) Assignment: Neither Party may assign this Agreement without the prior
    written consent of the other Party.
(f) Notices: All notices shall be delivered by email with read receipt or
    registered mail to the addresses set out on the signature page.
(g) Counterparts and Electronic Signatures: This Agreement may be executed
    in counterparts and by electronic signature, each of which shall be
    deemed an original and together constitute one instrument. Electronic
    signatures are valid under provincial electronic commerce legislation.

[FOR QUEBEC JURISDICTION — ADD:]
(h) Language: The Parties confirm that they have requested this Agreement
    to be drafted in English. Les parties confirment avoir demandé que la
    présente convention soit rédigée en anglais. (Charter of the French
    Language, CQLR c C-11, s. 55 compliance note.)

IN WITNESS WHEREOF, the Parties have executed this Agreement as of the date
first written above.

[PARTY A]                          [PARTY B]
By: ____________________           By: ____________________
Name:                              Name:
Title:                             Title:
Date:                              Date:
Address:                           Address:
Email:                             Email:
```

## Output Instructions
1. Fill in all [BRACKETED] fields based on user input
2. Select mutual or one-way sections as appropriate
3. Adjust duration based on industry norms:
   - Technology: 3–5 years
   - Employment: 2–3 years post-termination
   - M&A / investment: 2–3 years
4. For Quebec: offer French version option
5. Add disclaimer: "This template is a starting point. Have a Canadian lawyer review before signing."
