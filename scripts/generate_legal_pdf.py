#!/usr/bin/env python3
"""
AI Legal Assistant — Canadian Edition
PDF Report Generator

Generates professional, client-ready legal analysis reports formatted for
Canadian business use (CAD, Canadian statutes, provincial law references).

Requirements: pip3 install reportlab
Usage:
  python3 generate_legal_pdf.py \
    --title "Contract Review Report" \
    --jurisdiction "British Columbia" \
    --score 62 \
    --high 3 \
    --medium 5 \
    --low 4 \
    --output legal-report-20240101.pdf
"""

import argparse
import sys
import os
from datetime import datetime

# ---------------------------------------------------------------------------
# Check for reportlab
# ---------------------------------------------------------------------------
try:
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import letter
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch
    from reportlab.platypus import (
        SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
        HRFlowable, KeepTogether
    )
    from reportlab.graphics.shapes import Drawing, Wedge, Circle, String, Rect, Line
    from reportlab.graphics.charts.barcharts import HorizontalBarChart
    from reportlab.graphics import renderPDF
except ImportError:
    print("\n❌ reportlab is not installed.")
    print("   Install it with:  pip3 install reportlab")
    print("   Then re-run this script.\n")
    sys.exit(1)


# ---------------------------------------------------------------------------
# Canadian Brand Colors
# ---------------------------------------------------------------------------
NAVY    = colors.HexColor("#1B2A4A")   # Deep navy — professional Canadian firm
GOLD    = colors.HexColor("#C9972C")   # Gold accent
RED_CA  = colors.HexColor("#D42B2B")   # Canada red (for high risk)
AMBER   = colors.HexColor("#E07B00")   # Amber (medium risk)
GREEN   = colors.HexColor("#2E7D32")   # Green (low risk / compliant)
LIGHT   = colors.HexColor("#F5F7FA")   # Light background
MID     = colors.HexColor("#E8EBF0")   # Mid grey
WHITE   = colors.white
BLACK   = colors.HexColor("#1A1A1A")


# ---------------------------------------------------------------------------
# Province → Law Society Lookup
# ---------------------------------------------------------------------------
LAW_SOCIETIES = {
    "british columbia": ("Law Society of BC", "www.lawsociety.bc.ca"),
    "bc":               ("Law Society of BC", "www.lawsociety.bc.ca"),
    "alberta":          ("Law Society of Alberta", "www.lawsociety.ab.ca"),
    "ab":               ("Law Society of Alberta", "www.lawsociety.ab.ca"),
    "ontario":          ("Law Society of Ontario", "www.lso.ca"),
    "on":               ("Law Society of Ontario", "www.lso.ca"),
    "quebec":           ("Barreau du Québec", "www.barreau.qc.ca"),
    "qc":               ("Barreau du Québec", "www.barreau.qc.ca"),
    "manitoba":         ("Law Society of Manitoba", "www.lawsociety.mb.ca"),
    "mb":               ("Law Society of Manitoba", "www.lawsociety.mb.ca"),
    "saskatchewan":     ("Law Society of Saskatchewan", "www.lawsociety.sk.ca"),
    "sk":               ("Law Society of Saskatchewan", "www.lawsociety.sk.ca"),
    "nova scotia":      ("Nova Scotia Barristers' Society", "www.nsbs.org"),
    "ns":               ("Nova Scotia Barristers' Society", "www.nsbs.org"),
    "new brunswick":    ("Law Society of NB", "www.lawsociety-barreau.nb.ca"),
    "nb":               ("Law Society of NB", "www.lawsociety-barreau.nb.ca"),
    "newfoundland":     ("Law Society of NL", "www.lawsociety.nl.ca"),
    "nl":               ("Law Society of NL", "www.lawsociety.nl.ca"),
    "pei":              ("Law Society of PEI", "www.lspei.pe.ca"),
}


def get_law_society(jurisdiction: str):
    key = jurisdiction.lower().strip()
    return LAW_SOCIETIES.get(key, ("Canadian Bar Association", "www.cba.org"))


def score_to_grade(score: int) -> str:
    if score >= 85: return "A"
    if score >= 70: return "B"
    if score >= 55: return "C"
    if score >= 40: return "D"
    return "F"


def score_to_color(score: int):
    if score >= 70: return GREEN
    if score >= 50: return AMBER
    return RED_CA


def risk_color(level: str):
    level = level.upper()
    if "HIGH" in level: return RED_CA
    if "MEDIUM" in level or "MED" in level: return AMBER
    if "LOW" in level: return GREEN
    return NAVY


# ---------------------------------------------------------------------------
# Score Gauge (SVG-style drawing via ReportLab)
# ---------------------------------------------------------------------------
def make_score_gauge(score: int, width=220, height=130) -> Drawing:
    """Draw a simple semicircular score gauge."""
    d = Drawing(width, height)
    cx, cy = width / 2, height - 10
    r = min(cx, cy) - 10

    # Background arc segments (red / amber / green)
    import math
    segments = [
        (0,   40,  RED_CA),
        (40,  70,  AMBER),
        (70,  100, GREEN),
    ]
    for lo, hi, col in segments:
        start_angle = 180 - (lo / 100) * 180
        end_angle   = 180 - (hi / 100) * 180
        w = Wedge(cx, cy, r, end_angle, start_angle, strokeColor=None, fillColor=col)
        w.strokeWidth = 0
        d.add(w)

    # Inner white circle (donut effect)
    inner = Circle(cx, cy, r * 0.60, strokeColor=None, fillColor=WHITE)
    d.add(inner)

    # Needle
    angle_deg = 180 - (score / 100) * 180
    angle_rad = math.radians(angle_deg)
    nx = cx + (r * 0.75) * math.cos(angle_rad)
    ny = cy + (r * 0.75) * math.sin(angle_rad)
    d.add(Line(cx, cy, nx, ny, strokeColor=NAVY, strokeWidth=2.5))
    d.add(Circle(cx, cy, 5, fillColor=NAVY, strokeColor=None))

    # Score text
    grade = score_to_grade(score)
    d.add(String(cx, cy - 28, f"{score}", fontSize=22, fontName="Helvetica-Bold",
                 fillColor=score_to_color(score), textAnchor="middle"))
    d.add(String(cx, cy - 44, f"Grade: {grade}", fontSize=11, fontName="Helvetica",
                 fillColor=BLACK, textAnchor="middle"))
    d.add(String(cx, cy - 57, "Contract Safety Score", fontSize=8.5,
                 fontName="Helvetica", fillColor=colors.grey, textAnchor="middle"))

    return d


# ---------------------------------------------------------------------------
# Horizontal Risk Bar Chart
# ---------------------------------------------------------------------------
def make_risk_chart(high: int, medium: int, low: int, width=300, height=90) -> Drawing:
    d = Drawing(width, height)
    data = [(high,), (medium,), (low,)]
    max_val = max(high, medium, low, 1)

    bar_h = 18
    gap = 8
    labels = [f"High ({high})", f"Medium ({medium})", f"Low ({low})"]
    bar_colors = [RED_CA, AMBER, GREEN]
    label_x = 90

    for i, (val, label, col) in enumerate(zip([high, medium, low], labels, bar_colors)):
        y = height - (i + 1) * (bar_h + gap)
        bar_w = (val / max_val) * (width - label_x - 20) if max_val > 0 else 0
        # Label
        d.add(String(label_x - 5, y + 4, label, fontSize=8.5,
                     fontName="Helvetica", fillColor=BLACK, textAnchor="end"))
        # Bar background
        d.add(Rect(label_x, y, width - label_x - 20, bar_h,
                   fillColor=MID, strokeColor=None))
        # Bar fill
        if bar_w > 0:
            d.add(Rect(label_x, y, bar_w, bar_h, fillColor=col, strokeColor=None))

    return d


# ---------------------------------------------------------------------------
# Styles
# ---------------------------------------------------------------------------
def build_styles():
    base = getSampleStyleSheet()

    styles = {
        "h1": ParagraphStyle("h1", fontName="Helvetica-Bold",
                             fontSize=20, textColor=WHITE, leading=26),
        "h2": ParagraphStyle("h2", fontName="Helvetica-Bold",
                             fontSize=13, textColor=NAVY, spaceBefore=14, spaceAfter=6),
        "h3": ParagraphStyle("h3", fontName="Helvetica-Bold",
                             fontSize=10, textColor=NAVY, spaceBefore=8, spaceAfter=4),
        "body": ParagraphStyle("body", fontName="Helvetica",
                               fontSize=9.5, leading=14, textColor=BLACK),
        "small": ParagraphStyle("small", fontName="Helvetica",
                                fontSize=8, leading=12, textColor=colors.grey),
        "disclaimer": ParagraphStyle("disclaimer", fontName="Helvetica-Oblique",
                                     fontSize=8, leading=12, textColor=colors.grey,
                                     borderColor=GOLD, borderWidth=1,
                                     borderPadding=6, borderRadius=4),
        "label": ParagraphStyle("label", fontName="Helvetica-Bold",
                                fontSize=8.5, textColor=NAVY),
        "highlight": ParagraphStyle("highlight", fontName="Helvetica-Bold",
                                    fontSize=9.5, textColor=GOLD),
    }
    return styles


# ---------------------------------------------------------------------------
# Header / Footer
# ---------------------------------------------------------------------------
class CanadianLegalHeader:
    def __init__(self, title, jurisdiction, date_str):
        self.title = title
        self.jurisdiction = jurisdiction
        self.date_str = date_str

    def __call__(self, canvas, doc):
        canvas.saveState()
        w, h = letter

        # Navy header band
        canvas.setFillColor(NAVY)
        canvas.rect(0, h - 54, w, 54, fill=True, stroke=False)

        # Title
        canvas.setFillColor(WHITE)
        canvas.setFont("Helvetica-Bold", 14)
        canvas.drawString(0.5 * inch, h - 28, self.title)

        # Subtitle
        canvas.setFont("Helvetica", 9)
        canvas.drawString(0.5 * inch, h - 44,
                          f"Jurisdiction: {self.jurisdiction}  |  Currency: CAD  |  "
                          f"AI Legal Assistant — Canadian Edition")

        # Gold accent line
        canvas.setStrokeColor(GOLD)
        canvas.setLineWidth(2)
        canvas.line(0, h - 56, w, h - 56)

        # Footer
        canvas.setFont("Helvetica", 7.5)
        canvas.setFillColor(colors.grey)
        canvas.drawString(0.5 * inch, 0.35 * inch,
                          "AI Legal Assistant — Canadian Edition  |  "
                          "INFORMATIONAL USE ONLY — NOT LEGAL ADVICE  |  "
                          f"Prepared: {self.date_str}")
        canvas.drawRightString(w - 0.5 * inch, 0.35 * inch, f"Page {doc.page}")

        canvas.restoreState()


# ---------------------------------------------------------------------------
# Build PDF
# ---------------------------------------------------------------------------
def build_pdf(args):
    score       = max(0, min(100, args.score))
    high        = args.high
    medium      = args.medium
    low         = args.low
    jurisdiction = args.jurisdiction
    title       = args.title
    output_path = args.output
    notes       = args.notes or ""

    date_str = datetime.now().strftime("%B %d, %Y")
    grade    = score_to_grade(score)
    law_soc, ls_url = get_law_society(jurisdiction)
    styles   = build_styles()

    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        leftMargin=0.6 * inch,
        rightMargin=0.6 * inch,
        topMargin=1.1 * inch,
        bottomMargin=0.7 * inch,
    )
    header_fn = CanadianLegalHeader(title, jurisdiction, date_str)
    story = []

    # ── Cover Info ──────────────────────────────────────────────────────────
    cover_data = [
        ["Report Title:", title],
        ["Jurisdiction:", f"{jurisdiction} — Canadian Law"],
        ["Currency:", "Canadian Dollars (CAD)"],
        ["Prepared:", date_str],
        ["Classification:", "CONFIDENTIAL — For Review Purposes Only"],
    ]
    cover_table = Table(cover_data, colWidths=[1.5 * inch, 5.2 * inch])
    cover_table.setStyle(TableStyle([
        ("FONTNAME",  (0, 0), (0, -1), "Helvetica-Bold"),
        ("FONTNAME",  (1, 0), (1, -1), "Helvetica"),
        ("FONTSIZE",  (0, 0), (-1, -1), 9.5),
        ("TEXTCOLOR", (0, 0), (0, -1), NAVY),
        ("TEXTCOLOR", (1, 0), (1, -1), BLACK),
        ("ROWBACKGROUNDS", (0, 0), (-1, -1), [LIGHT, WHITE]),
        ("TOPPADDING",    (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING",   (0, 0), (-1, -1), 8),
    ]))
    story.append(cover_table)
    story.append(Spacer(1, 0.2 * inch))

    # ── Score + Risk Chart Side by Side ─────────────────────────────────────
    story.append(Paragraph("Executive Summary", styles["h2"]))
    story.append(HRFlowable(width="100%", thickness=1.5, color=GOLD))
    story.append(Spacer(1, 0.1 * inch))

    gauge = make_score_gauge(score, width=200, height=120)
    chart = make_risk_chart(high, medium, low, width=290, height=100)

    summary_table = Table(
        [[gauge, chart]],
        colWidths=[2.8 * inch, 4.0 * inch],
    )
    summary_table.setStyle(TableStyle([
        ("VALIGN",      (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
    ]))
    story.append(summary_table)
    story.append(Spacer(1, 0.15 * inch))

    # Risk stats row
    total = high + medium + low
    risk_stats = [
        ["🔴 High Risk", "🟡 Medium Risk", "🟢 Low Risk", "Total Clauses"],
        [str(high), str(medium), str(low), str(total)],
    ]
    rs_table = Table(risk_stats, colWidths=[1.65 * inch] * 4)
    rs_table.setStyle(TableStyle([
        ("ALIGN",        (0, 0), (-1, -1), "CENTER"),
        ("FONTNAME",     (0, 0), (-1, 0),  "Helvetica-Bold"),
        ("FONTNAME",     (0, 1), (-1, 1),  "Helvetica-Bold"),
        ("FONTSIZE",     (0, 0), (-1, -1), 9.5),
        ("TEXTCOLOR",    (0, 1), (0, 1),   RED_CA),
        ("TEXTCOLOR",    (1, 1), (1, 1),   AMBER),
        ("TEXTCOLOR",    (2, 1), (2, 1),   GREEN),
        ("TEXTCOLOR",    (3, 1), (3, 1),   NAVY),
        ("ROWBACKGROUNDS", (0, 0), (-1, -1), [MID, LIGHT]),
        ("TOPPADDING",   (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING",(0, 0), (-1, -1), 6),
        ("GRID",         (0, 0), (-1, -1), 0.3, colors.grey),
    ]))
    story.append(rs_table)

    if notes:
        story.append(Spacer(1, 0.15 * inch))
        story.append(Paragraph("Key Findings", styles["h3"]))
        story.append(Paragraph(notes, styles["body"]))

    story.append(Spacer(1, 0.2 * inch))

    # ── Canadian Compliance Status ───────────────────────────────────────────
    story.append(Paragraph("Canadian Compliance Status", styles["h2"]))
    story.append(HRFlowable(width="100%", thickness=1.5, color=GOLD))
    story.append(Spacer(1, 0.1 * inch))

    compliance_data = [
        ["Framework", "Status", "Statute / Reference", "Max Fine (CAD)"],
        ["PIPEDA (Federal Privacy)", "⚠️ Review", "S.C. 2000, c. 5", "$100,000"],
        ["Law 25 (Quebec)", "N/A or ⚠️", "CQLR c P-63.1", "$25M / 4% revenue"],
        ["CASL", "⚠️ Review", "S.C. 2010, c. 23", "$10M / violation"],
        ["Employment Standards", "⚠️ Review", "Provincial ESA", "Variable"],
        ["Competition Act", "✅ N/A", "R.S.C. 1985, c. C-34", "$10M"],
        ["Consumer Protection", "⚠️ Review", "Provincial CPA", "Variable"],
        ["AODA (Ontario)", "N/A", "S.O. 2005, c. 11", "$100,000/day"],
    ]
    comp_table = Table(compliance_data, colWidths=[2.0 * inch, 1.0 * inch, 2.3 * inch, 1.35 * inch])
    comp_table.setStyle(TableStyle([
        ("FONTNAME",       (0, 0), (-1, 0),  "Helvetica-Bold"),
        ("FONTNAME",       (0, 1), (-1, -1), "Helvetica"),
        ("FONTSIZE",       (0, 0), (-1, -1), 8.5),
        ("BACKGROUND",     (0, 0), (-1, 0),  NAVY),
        ("TEXTCOLOR",      (0, 0), (-1, 0),  WHITE),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [LIGHT, WHITE]),
        ("ALIGN",          (1, 0), (1, -1),  "CENTER"),
        ("ALIGN",          (3, 0), (3, -1),  "RIGHT"),
        ("TOPPADDING",     (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING",  (0, 0), (-1, -1), 5),
        ("LEFTPADDING",    (0, 0), (-1, -1), 6),
        ("GRID",           (0, 0), (-1, -1), 0.3, colors.lightgrey),
    ]))
    story.append(comp_table)
    story.append(Spacer(1, 0.1 * inch))
    story.append(Paragraph(
        "Note: Status indicators above are placeholders. Replace with actual findings from /legal review.",
        styles["small"]
    ))

    story.append(Spacer(1, 0.2 * inch))

    # ── Action Plan ──────────────────────────────────────────────────────────
    story.append(Paragraph("Recommended Action Plan", styles["h2"]))
    story.append(HRFlowable(width="100%", thickness=1.5, color=GOLD))
    story.append(Spacer(1, 0.1 * inch))

    action_data = [
        ["Priority", "Action", "Timeline", "CAD Impact"],
        ["🔴 Critical", "Review and renegotiate high-risk clauses", "Before signing", "High"],
        ["🔴 Critical", "Ensure PIPEDA/Law 25 compliance language", "Before signing", "Up to $25M"],
        ["🟡 Medium", "Add missing protections (IP, privacy, force majeure)", "Before signing", "Moderate"],
        ["🟡 Medium", "Review termination clause against ESA minimums", "Before signing", "Significant"],
        ["🟢 Low", "Clarify ambiguous payment terms and late penalties", "At signing", "Low"],
        ["📋 Post-sign", "Schedule compliance review in 12 months", "Within 1 year", "Preventive"],
    ]
    action_table = Table(action_data, colWidths=[1.0 * inch, 3.2 * inch, 1.2 * inch, 1.25 * inch])
    action_table.setStyle(TableStyle([
        ("FONTNAME",       (0, 0), (-1, 0),  "Helvetica-Bold"),
        ("FONTNAME",       (0, 1), (-1, -1), "Helvetica"),
        ("FONTSIZE",       (0, 0), (-1, -1), 8.5),
        ("BACKGROUND",     (0, 0), (-1, 0),  NAVY),
        ("TEXTCOLOR",      (0, 0), (-1, 0),  WHITE),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [LIGHT, WHITE]),
        ("TOPPADDING",     (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING",  (0, 0), (-1, -1), 5),
        ("LEFTPADDING",    (0, 0), (-1, -1), 6),
        ("GRID",           (0, 0), (-1, -1), 0.3, colors.lightgrey),
        ("VALIGN",         (0, 0), (-1, -1), "TOP"),
    ]))
    story.append(action_table)

    story.append(Spacer(1, 0.25 * inch))

    # ── Find a Canadian Lawyer ───────────────────────────────────────────────
    story.append(Paragraph("Find a Licensed Canadian Lawyer", styles["h2"]))
    story.append(HRFlowable(width="100%", thickness=1.5, color=GOLD))
    story.append(Spacer(1, 0.1 * inch))

    lawyer_text = (
        f"For the Province of <b>{jurisdiction}</b>, contact the "
        f"<b>{law_soc}</b> to find a licensed lawyer (barrister/solicitor): "
        f"<b>{ls_url}</b><br/><br/>"
        "Other resources:<br/>"
        "• Canadian Bar Association (national): www.cba.org<br/>"
        "• Law Help Ontario (free legal help): www.lawhelpontario.org<br/>"
        "• Centre for Public Legal Education Alberta: www.cplea.ca<br/>"
        "• Éducaloi (Quebec, bilingual): www.educaloi.qc.ca<br/>"
        "• People's Law School (BC): www.peopleslawschool.ca"
    )
    story.append(Paragraph(lawyer_text, styles["body"]))

    story.append(Spacer(1, 0.25 * inch))

    # ── Disclaimer ───────────────────────────────────────────────────────────
    story.append(Paragraph("⚠️  Legal Disclaimer", styles["h2"]))
    story.append(HRFlowable(width="100%", thickness=1.5, color=GOLD))
    story.append(Spacer(1, 0.1 * inch))

    disclaimer = (
        "This report was generated by an AI system and is provided for "
        "INFORMATIONAL AND EDUCATIONAL PURPOSES ONLY. It does NOT constitute "
        "legal advice and does NOT create a lawyer-client relationship. "
        "The analysis reflects general Canadian legal principles and may not "
        "account for specific facts, recent statutory changes, or provincial "
        "variations that apply to your situation.<br/><br/>"
        "You should NOT rely on this report as a substitute for professional "
        "legal advice from a qualified Canadian lawyer (barrister/solicitor) "
        "who is licensed to practice in the relevant province or territory. "
        "Always have a licensed legal professional review any contract before "
        "signing.<br/><br/>"
        "Canadian law varies significantly by province. Quebec is governed by "
        "the Civil Code of Quebec; all other provinces operate under common law. "
        "Federal statutes (PIPEDA, CASL, Canada Labour Code) apply nationally "
        "but interact with provincial legislation in complex ways."
    )
    story.append(Paragraph(disclaimer, styles["disclaimer"]))

    # ── Build ────────────────────────────────────────────────────────────────
    doc.build(story, onFirstPage=header_fn, onLaterPages=header_fn)
    print(f"\n✅ PDF generated: {output_path}")
    size_kb = os.path.getsize(output_path) // 1024
    print(f"   Size: {size_kb} KB\n")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(
        description="AI Legal Assistant — Canadian Edition PDF Generator"
    )
    parser.add_argument("--title",        default="Contract Review Report",
                        help="Report title")
    parser.add_argument("--jurisdiction", default="Canada",
                        help="Province or territory (e.g., 'British Columbia', 'Ontario')")
    parser.add_argument("--score",        type=int, default=50,
                        help="Contract Safety Score (0–100)")
    parser.add_argument("--high",         type=int, default=0,
                        help="Number of high-risk clauses")
    parser.add_argument("--medium",       type=int, default=0,
                        help="Number of medium-risk clauses")
    parser.add_argument("--low",          type=int, default=0,
                        help="Number of low-risk clauses")
    parser.add_argument("--notes",        default="",
                        help="Key findings / executive summary text")
    parser.add_argument("--output",       default="legal-report.pdf",
                        help="Output PDF file path")

    args = parser.parse_args()
    build_pdf(args)


if __name__ == "__main__":
    main()
