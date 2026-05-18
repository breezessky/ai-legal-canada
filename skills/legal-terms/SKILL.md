# Skill: /legal terms

## Purpose
Generate Terms of Service / Terms of Use for Canadian websites and apps — compliant with CASL, provincial Consumer Protection Acts, and PIPEDA/Law 25.

## Trigger
`/legal terms <url>`

## Canadian Legal Requirements

### CASL (Canada's Anti-Spam Legislation, S.C. 2010, c. 23)
- Express or implied consent required before sending Commercial Electronic Messages (CEMs)
- Identify sender clearly
- Provide working unsubscribe mechanism (must process within 10 business days)
- CASL applies to all electronic messages sent FROM Canada or TO Canadian recipients
- Fines: up to CAD $1M (individuals), CAD $10M (organizations) per violation

### Consumer Protection Acts (Provincial)
- **Ontario**: *Consumer Protection Act, 2002*, S.O. 2002, c. 30 — governs online transactions, cooling-off periods, internet agreements
- **BC**: *Business Practices and Consumer Protection Act*, S.B.C. 2004, c. 2
- **Alberta**: *Fair Trading Act*, R.S.A. 2000, c. F-2
- **Quebec**: *Consumer Protection Act*, CQLR c P-40.1 — strictest in Canada; prohibits certain limitation clauses in consumer contracts

### Key Quebec Requirements
- Terms must be readable and comprehensible (art. 1436 CCQ — abusive clauses void)
- Must be available in French (Charter of the French Language, Bill 96)
- No hidden fees; price must be prominently disclosed
- Consumer has 7-day cooling-off period for distance contracts

### Digital Commerce Requirements
- Subscription auto-renewal: disclosure requirements under Ontario *Consumer Protection Act*
- Price transparency: all amounts in CAD with taxes disclosed
- Dispute resolution clause cannot mandate foreign jurisdiction for BC/ON/QC consumers

## Process
1. Fetch and scan the URL provided
2. Identify: business type, products/services, data collected, payment model, jurisdiction
3. Generate compliant Terms of Service

## Generated Terms of Service Template

```markdown
TERMS OF SERVICE / CONDITIONS D'UTILISATION
Last Updated: [DATE]

PLEASE READ THESE TERMS CAREFULLY BEFORE USING [WEBSITE/APP NAME].
By accessing or using [website] (the "Service"), you agree to be bound
by these Terms of Service ("Terms"). If you do not agree, do not use
the Service.

1. PARTIES AND ACCEPTANCE

These Terms constitute a legally binding agreement between:
  [COMPANY LEGAL NAME], [incorporated/registered] under the laws of
  [Province], with its principal office at [ADDRESS]
  ("Company", "we", "us", or "our")

  AND

  You, the individual or entity accessing the Service ("you" or "User").

2. DESCRIPTION OF SERVICE

[Description of what the service does]

3. ELIGIBILITY

To use the Service, you must:
(a) Be at least 18 years of age (or the age of majority in your province);
(b) Have the legal capacity to enter into contracts;
(c) Not be prohibited from using the Service under applicable Canadian law.

4. ACCOUNTS

If the Service requires account creation:
(a) You are responsible for maintaining the confidentiality of your credentials;
(b) You are responsible for all activity under your account;
(c) Notify us immediately at [EMAIL] of any unauthorized access.

5. ACCEPTABLE USE

You agree NOT to:
(a) Use the Service for any unlawful purpose under Canadian federal or
    provincial law;
(b) Violate the *Criminal Code of Canada*, the *Competition Act*, or
    applicable provincial statutes;
(c) Send spam or unsolicited commercial electronic messages in violation
    of CASL;
(d) Engage in fraudulent, deceptive, or misleading conduct contrary to
    the *Competition Act*, R.S.C. 1985, c. C-34;
(e) Infringe any intellectual property rights under the *Copyright Act*,
    *Trade-marks Act*, or *Patent Act*.

6. ELECTRONIC COMMUNICATIONS AND CASL COMPLIANCE

By creating an account or making a purchase, you provide express consent to
receive transactional and service-related electronic messages.

Marketing communications: We will only send marketing messages if you have
provided express consent. You may withdraw consent at any time by clicking
"Unsubscribe" in any marketing email or contacting us at [EMAIL]. We will
process unsubscribe requests within 10 business days, as required by CASL.

7. PRICING AND PAYMENT (CAD)

(a) All prices are in Canadian Dollars (CAD) unless otherwise stated;
(b) Applicable GST/HST/PST/QST will be added at checkout;
(c) [PAYMENT PROCESSOR] processes payments; [Company] does not store
    full credit card information;
(d) [Subscription terms, billing cycle, and cancellation policy if applicable].

8. AUTO-RENEWAL (IF APPLICABLE)

Your subscription will automatically renew at the end of each billing period.
We will notify you at least [X] days before renewal. You may cancel at any
time through your account settings. Ontario residents: cancellation rights
apply under the *Consumer Protection Act, 2002*.

9. REFUNDS AND RETURNS

[Refund policy — note: Quebec consumers have statutory 7-day cooling-off
period for distance contracts under the *Consumer Protection Act*, CQLR c P-40.1]

10. INTELLECTUAL PROPERTY

All content on the Service — including text, graphics, logos, images,
and software — is owned by or licensed to [Company] and protected by the
*Copyright Act*, R.S.C. 1985, c. C-42. You may not reproduce, distribute,
or create derivative works without written permission.

11. PRIVACY

Your privacy is governed by our Privacy Policy, which is incorporated into
these Terms and complies with the *Personal Information Protection and
Electronic Documents Act* (PIPEDA), S.C. 2000, c. 5, and applicable
provincial privacy legislation including Quebec's *Act respecting the
protection of personal information in the private sector* (Law 25).

12. DISCLAIMER OF WARRANTIES

THE SERVICE IS PROVIDED "AS IS" WITHOUT WARRANTIES OF ANY KIND. TO THE
MAXIMUM EXTENT PERMITTED BY CANADIAN LAW, WE DISCLAIM ALL WARRANTIES,
EXPRESS OR IMPLIED.

Note: Consumer protection statutes in certain provinces (particularly Quebec)
may provide implied warranties that cannot be disclaimed.

13. LIMITATION OF LIABILITY

TO THE MAXIMUM EXTENT PERMITTED BY APPLICABLE CANADIAN LAW, [COMPANY]'S
TOTAL LIABILITY FOR ANY CLAIM ARISING FROM USE OF THE SERVICE SHALL NOT
EXCEED THE GREATER OF: (A) CAD $[AMOUNT]; OR (B) THE FEES PAID BY YOU
IN THE PRECEDING 12 MONTHS.

NOTHING IN THESE TERMS LIMITS LIABILITY FOR FRAUD, GROSS NEGLIGENCE,
DEATH OR PERSONAL INJURY CAUSED BY NEGLIGENCE, OR ANY OTHER LIABILITY
THAT CANNOT BE LIMITED UNDER APPLICABLE LAW.

14. INDEMNIFICATION

You agree to indemnify and hold harmless [Company] from any claims,
damages, and expenses (including reasonable legal fees) arising from
your violation of these Terms or applicable law.

15. GOVERNING LAW AND DISPUTE RESOLUTION

These Terms are governed by the laws of the Province of [PROVINCE] and
the federal laws of Canada applicable therein.

Consumer disputes: Nothing in these Terms prevents you from exercising
your rights under applicable provincial consumer protection legislation.

Dispute resolution: The Parties agree to first attempt to resolve any
dispute through good-faith negotiation. [Optional: binding arbitration
under [Province] Arbitration Act / courts of [Province]].

Class actions: [If waiving class actions — note this is not enforceable
in Quebec under the *Code of Civil Procedure*, CQLR c C-25.01]

16. MODIFICATIONS

We may modify these Terms at any time. We will provide [30] days' notice
of material changes by email or prominent website notice. Continued use
after the effective date constitutes acceptance of the modified Terms.

17. TERMINATION

We may suspend or terminate your access for violation of these Terms.
You may terminate by deleting your account. Sections 10, 11, 12, 13,
15, and this Section survive termination.

18. GENERAL

(a) Entire Agreement: These Terms (with the Privacy Policy) constitute
    the entire agreement regarding the Service.
(b) Severability: If any provision is found invalid, the remainder continues.
(c) Language: These Terms are in English. [For Quebec:] Les présentes
    conditions sont également disponibles en français sur demande.
(d) Contact: [COMPANY NAME], [ADDRESS], [EMAIL], [PHONE]

[COMPANY NAME]
[ADDRESS]
[CITY, PROVINCE, POSTAL CODE]
[EMAIL] | [PHONE]
```

## Output Instructions
1. Scan the URL to identify the business type and services
2. Fill in all [BRACKETED] fields
3. Highlight CASL consent mechanism requirements
4. Flag if Quebec users are served (French version required)
5. Add disclaimer at the end
