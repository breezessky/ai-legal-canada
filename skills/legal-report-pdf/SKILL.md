# Skill: /legal report-pdf

## Purpose
Generate a professional, client-ready PDF report from the results of any `/legal` analysis. Outputs a branded document with score gauges, risk charts, and prioritized actions — formatted for Canadian business use (CAD, Canadian statutes).

## Trigger
`/legal report-pdf`

## Prerequisites
- Python 3.8+
- reportlab: `pip3 install reportlab`

## Process
1. Collect results from the most recent `/legal` analysis in the session
2. Run `generate_legal_pdf.py` to produce the PDF
3. Save to `./legal-report-[timestamp].pdf`
4. Confirm output path to user

## Output Call

```bash
python3 ~/.claude/skills/legal/scripts/generate_legal_pdf.py \
  --title "Contract Review Report" \
  --jurisdiction "[Province]" \
  --score [0-100] \
  --high [n] \
  --medium [n] \
  --low [n] \
  --output "legal-report-$(date +%Y%m%d).pdf"
```

## Report Sections

1. **Cover Page**
   - Report title
   - Date prepared
   - Jurisdiction (Province) | Currency: CAD
   - "CONFIDENTIAL — For Review Purposes Only"
   - Disclaimer: "Not legal advice. Consult a licensed Canadian lawyer."

2. **Executive Summary**
   - Contract Safety Score gauge (0–100)
   - Letter grade (A/B/C/D/F)
   - Key findings in 3–5 bullets

3. **Risk Dashboard**
   - Horizontal bar chart: High / Medium / Low risk counts
   - Compliance status table: PIPEDA / CASL / Law 25 / ESA / Consumer Protection

4. **Clause Analysis** (table format)
   - Clause | Risk Level | Plain English Summary | Recommendation

5. **Compliance Summary**
   - Per-framework status with ✅ / ⚠️ / 🔴
   - Fine exposure table in CAD

6. **Negotiation Priorities**
   - Ranked list with CAD exposure estimates

7. **Missing Protections**
   - Checklist of absent clauses

8. **Action Plan**
   - Prioritized, dated checklist
   - Immediate / 30-day / 90-day horizon

9. **Disclaimer & Contact**
   - Standard Canadian legal disclaimer
   - "Have a licensed Canadian lawyer (barrister/solicitor) review before signing"
   - Law Society contacts by province

## Styling
- Colors: Deep navy (#1B2A4A) header, gold (#C9972C) accents (professional Canadian financial firm aesthetic)
- Font: Helvetica (bundled with reportlab) or DejaVu if available
- All amounts: CAD $X,XXX format
- Footer: "AI Legal Assistant — Canadian Edition | Informational Use Only"

## Provincial Law Society Quick Reference (for disclaimer page)
| Province | Law Society | Website |
|----------|-------------|---------|
| BC | Law Society of BC | www.lawsociety.bc.ca |
| AB | Law Society of Alberta | www.lawsociety.ab.ca |
| SK | Law Society of Saskatchewan | www.lawsociety.sk.ca |
| MB | Law Society of Manitoba | www.lawsociety.mb.ca |
| ON | Law Society of Ontario | www.lso.ca |
| QC | Barreau du Québec | www.barreau.qc.ca |
| NB | Law Society of New Brunswick | www.lawsociety-barreau.nb.ca |
| NS | Nova Scotia Barristers' Society | www.nsbs.org |
| PEI | Law Society of PEI | www.lspei.pe.ca |
| NL | Law Society of Newfoundland | www.lawsociety.nl.ca |
| YT/NT/NU | Contact federal / territorial bar associations | |

## Error Handling
If reportlab is not installed:
```
⚠️ reportlab is required for PDF generation.
Install with: pip3 install reportlab
Then re-run: /legal report-pdf
```
