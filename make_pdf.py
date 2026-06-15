"""
Generate PDF for Dario Amodei's "Policy on the AI Exponential" (June 10, 2026)
Using reportlab to produce a clean, readable document from researched content.
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, black, white, grey
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, HRFlowable, ListFlowable, ListItem
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY

OUTPUT = "/home/user/AI-world-view/Dario Amodei Policy on the AI Exponential.pdf"

doc = SimpleDocTemplate(
    OUTPUT,
    pagesize=letter,
    rightMargin=1*inch,
    leftMargin=1*inch,
    topMargin=1*inch,
    bottomMargin=1*inch,
    title="Policy on the AI Exponential",
    author="Dario Amodei",
)

ACCENT = HexColor("#1e2e8e")
LIGHT_GRAY = HexColor("#f0f0f0")
MID_GRAY = HexColor("#888888")

styles = getSampleStyleSheet()

title_style = ParagraphStyle(
    "DocTitle",
    fontName="Helvetica-Bold",
    fontSize=24,
    leading=30,
    textColor=ACCENT,
    spaceAfter=6,
    alignment=TA_CENTER,
)
byline_style = ParagraphStyle(
    "Byline",
    fontName="Helvetica",
    fontSize=12,
    textColor=MID_GRAY,
    spaceAfter=4,
    alignment=TA_CENTER,
)
note_style = ParagraphStyle(
    "Note",
    fontName="Helvetica-Oblique",
    fontSize=9,
    textColor=MID_GRAY,
    spaceAfter=8,
    leading=12,
)
section_style = ParagraphStyle(
    "SectionHead",
    fontName="Helvetica-Bold",
    fontSize=14,
    textColor=ACCENT,
    spaceBefore=12,
    spaceAfter=4,
    leading=18,
)
body_style = ParagraphStyle(
    "Body",
    fontName="Helvetica",
    fontSize=11,
    leading=16,
    spaceAfter=8,
    alignment=TA_JUSTIFY,
)
quote_style = ParagraphStyle(
    "Quote",
    fontName="Helvetica-Oblique",
    fontSize=11,
    leading=16,
    spaceAfter=8,
    leftIndent=24,
    rightIndent=24,
    textColor=HexColor("#444444"),
)
footer_style = ParagraphStyle(
    "Footer",
    fontName="Helvetica-Oblique",
    fontSize=9,
    textColor=MID_GRAY,
    leading=12,
    spaceAfter=4,
)

def section(title):
    return [Paragraph(title, section_style), HRFlowable(color=ACCENT, thickness=0.5, spaceAfter=6)]

def body(text):
    return Paragraph(text, body_style)

def quote(text):
    return Paragraph(f'"{text}"', quote_style)

def bullets(items):
    return ListFlowable(
        [ListItem(Paragraph(item, body_style), leftIndent=20, bulletIndent=8) for item in items],
        bulletType="bullet",
        bulletColor=ACCENT,
        spaceAfter=8,
    )

story = []

# ── Title ────────────────────────────────────────────────────────────────────
story.append(Spacer(1, 0.2*inch))
story.append(Paragraph("Policy on the AI Exponential", title_style))
story.append(Paragraph("Dario Amodei  |  CEO, Anthropic", byline_style))
story.append(Paragraph("Published June 10, 2026  |  darioamodei.com/post/policy-on-the-ai-exponential", byline_style))
story.append(Spacer(1, 0.1*inch))
story.append(HRFlowable(color=ACCENT, thickness=1.5, spaceAfter=8))
story.append(Paragraph(
    "Note: This document was compiled from publicly available summaries and press coverage "
    "of the essay as part of the AI World View canon maintenance process. "
    "The full original essay is available at darioamodei.com.",
    note_style,
))
story.append(Spacer(1, 0.1*inch))

# ── Overview ─────────────────────────────────────────────────────────────────
story += section("Overview")
story.append(body(
    "In \"Policy on the AI Exponential,\" Anthropic CEO Dario Amodei argues that AI capabilities "
    "are compounding faster than legislatures can respond — and that the moment for voluntary, "
    "transparency-based AI governance has passed. The essay marks a significant public evolution "
    "for Amodei and Anthropic: after helping to pass transparency legislation in California (SB 53), "
    "New York (RAISE), and Illinois (SB 315) in 2025–2026, he now argues those measures are "
    "necessary but insufficient."
))
story.append(body(
    "The essay covers five policy domains where governments must act: "
    "(1) frontier-model safety regulation, (2) job displacement and macroeconomic policy, "
    "(3) accelerating beneficial scientific uses of AI, (4) protecting civil liberties from "
    "AI-enabled state and corporate power, and (5) securing democratic leadership in the global "
    "AI race. Alongside the essay, Anthropic released an Advanced AI Framework and an Economic "
    "Policy Framework backed by $350 million in new financial commitments."
))
story.append(body(
    "Amodei uses a Tolkien analogy to frame the central challenge: policy institutions move at "
    "the pace of a walking journey, while AI capabilities are advancing at the speed of an eagle. "
    "His core thesis is that the gap between capability advancement and policy response is now "
    "dangerous enough to require binding, enforceable regulation — not merely transparency or "
    "voluntary commitments."
))

# ── Section 1 ─────────────────────────────────────────────────────────────────
story += section("I.  Frontier Model Safety Regulation")
story.append(body(
    "The centerpiece of the essay is a proposal modeled on the FAA and pharmaceutical regulatory "
    "frameworks. Frontier AI models above a specified compute threshold would undergo mandatory "
    "third-party testing across four risk categories before deployment:"
))
story.append(bullets([
    "Cybersecurity — capability to enable large-scale attacks on critical infrastructure.",
    "Biological weapons — ability to assist in creating weapons of mass destruction.",
    "Loss of control — potential for the model to act in ways that undermine human oversight.",
    "Automated R&D acceleration — potential to autonomously advance its own capabilities in ways "
    "that compound the above three risks.",
]))
story.append(body(
    "The government would have explicit authority to block or delay deployment if testing reveals "
    "unacceptable risk in any of these four areas. Amodei proposes this power be strictly scoped — "
    "explicitly excluding content moderation, fairness, or other socially contested uses — and "
    "that procedural safeguards prevent political favoritism or arbitrary decisions."
))
story.append(body(
    "Third-party evaluation could be conducted by a government agency (FAA-style), a set of private "
    "organizations authorized and inspected by the government (a \"regulatory markets\" model), "
    "or a hybrid. The core requirement is binding pre-deployment testing with government blocking "
    "authority — not mere disclosure. This represents a meaningful escalation from Anthropic's "
    "prior position of transparency mandates."
))

# ── Section 2 ─────────────────────────────────────────────────────────────────
story += section("II.  Job Displacement and Macroeconomic Policy")
story.append(body(
    "Amodei takes a notably candid position on labor displacement, acknowledging that adaptive "
    "mechanisms economists traditionally invoke — Jevons paradox and comparative advantage — "
    "may be overwhelmed by the speed of the technology."
))
story.append(quote(
    "If AI-driven labor displacement ends up being large in magnitude and permanently drives down "
    "the demand for labor, it will likely be necessary to go beyond mere incentive programs to "
    "long-term income support for a significant fraction of the labor force."
))
story.append(body("He proposes a graduated policy response scaled to the degree of displacement observed:"))
story.append(bullets([
    "Measurement first: Expand government economic statistics to track AI-driven displacement at "
    "sector and occupation level, building on Anthropic's own Economic Index for Claude usage.",
    "Pro-employment incentives: Wage insurance (paying the difference when workers accept lower-paying "
    "jobs), employer retention tax incentives, and retraining grants.",
    "Long-term income support: If displacement proves large and permanent, graduated universal basic "
    "income financed through taxes on AI companies or increased capital gains taxes.",
    "Claude Corps: Alongside the essay, Anthropic announced an $85,000 fellowship explicitly "
    "acknowledging the company's role in potential displacement.",
]))
story.append(body(
    "Amodei does not argue AI will create enough new jobs to offset displacement. He argues policy "
    "should be designed to respond proportionately to whatever level of displacement actually occurs — "
    "and that current frameworks are not calibrated for a potential permanent reduction in labor demand."
))

# ── Section 3 ─────────────────────────────────────────────────────────────────
story += section("III.  Accelerating Beneficial Scientific Uses of AI")
story.append(body(
    "On scientific acceleration, Amodei inverts the usual regulatory concern. For most AI applications, "
    "the regulatory worry is that oversight will be too slow to catch risks. For fields like biomedicine "
    "and materials science, his argument is the opposite: regulatory systems designed for a slower "
    "pace of innovation will become bottlenecks preventing AI from delivering its scientific benefits."
))
story.append(body(
    "The FDA and EMA should define — before the AI-assisted drug discovery pipeline is ready to deliver "
    "at scale — what evidence standards will accept AI-based methods: toxicology prediction, synthetic "
    "control arms in clinical trials, AI-assisted pathology review. The 7–8 year approval pipeline will "
    "otherwise become the constraint, not the underlying science."
))
story.append(body(
    "He advocates for regulatory pre-commitment: agencies publishing clear acceptance criteria for "
    "AI-assisted methods in advance, so researchers can design toward known standards. This parallels "
    "how the FDA's 'breakthrough therapy' designation created an accelerated pathway — a template for "
    "regulatory innovation matching scientific innovation."
))

# ── Section 4 ─────────────────────────────────────────────────────────────────
story += section("IV.  Civil Liberties and AI-Enabled Power")
story.append(body(
    "Amodei argues that AI dramatically amplifies both state and corporate capacity for surveillance, "
    "manipulation, and control. He proposes four specific safeguards:"
))
story.append(bullets([
    "Ban autonomous lethal weapons from domestic use — AI systems capable of lethal action should "
    "not be deployed in law enforcement or domestic security contexts.",
    "Close bulk data purchase loopholes — current law allows government agencies to buy from private "
    "data brokers information they could not directly collect without a warrant. AI makes this loophole "
    "far more consequential.",
    "Guarantee legal AI parity — citizens should have access to AI systems of equal capability to "
    "those used by government or prosecutors in legal proceedings against them.",
    "Mandatory disclosure of AI use — any significant AI-assisted decision affecting citizens "
    "(benefits, sentencing, credit) should require disclosure of AI's role.",
]))
story.append(body(
    "The civil liberties section reflects concern that concentration of AI capability in states or "
    "large corporations could fundamentally destabilize the conditions under which democratic "
    "self-governance functions — framed as an active concern given current capabilities, not a future risk."
))

# ── Section 5 ─────────────────────────────────────────────────────────────────
story += section("V.  Geopolitics and Democratic AI Leadership")
story.append(body(
    "The final section calls for democratic nations to form an exclusive coalition to control the global "
    "AI supply chain — a framework The Decoder described as \"a Cold War playbook for the AI age.\""
))
story.append(body("Amodei proposes that the US and allied democracies coordinate to:"))
story.append(bullets([
    "Control chip manufacturing and export — deny leading-edge AI semiconductors and manufacturing "
    "equipment to non-allied nations.",
    "Build a values-aligned AI coalition — prioritize sharing AI economic and scientific benefits "
    "within the coalition and excluding adversarial states.",
    "Coordinate on mutual defense — AI capabilities relevant to national security treated as a "
    "shared asset of the democratic coalition, not merely bilateral US advantage.",
    "Internationalize AI governance standards — jointly develop and enforce the safety testing "
    "standards proposed in Section I, preventing a race to the regulatory bottom.",
]))
story.append(body(
    "This escalates from Amodei's previous geopolitical writing (\"On DeepSeek and Export Controls,\" "
    "2026), which focused primarily on chip export controls as a US national security tool. "
    "\"Policy on the AI Exponential\" frames the question as fundamentally about which political "
    "systems shape the AI acceleration — and argues democratic values must be built into the "
    "supply chain, not merely advocated for."
))

# ── Worldview Implications ────────────────────────────────────────────────────
story += section("Significance and Worldview Implications")
story.append(bullets([
    "Regulatory framing update: The worldview currently notes 'regulatory uncertainty is no longer "
    "a valid excuse.' Amodei adds a new layer: existing frameworks may be insufficient even for "
    "willing actors, and binding pre-deployment testing is the next required step.",
    "Labor displacement: This is the most candid acknowledgment from a frontier lab CEO that "
    "large-scale permanent displacement is a real possibility — materially updating the 'augmentation "
    "before automation' framing in the current worldview.",
    "Geopolitical dimension: The current worldview does not address supply chain and coalition "
    "dynamics. Amodei's framework suggests these will determine which values shape AI globally — "
    "relevant to community banks through vendor consolidation and regulatory jurisdiction risk.",
    "Science acceleration: The proposal for FDA/EMA pre-commitment on AI-assisted methods suggests "
    "GDP and productivity impact estimates (Goldman 7%, Brynjolfsson 14–34%) may be conservative "
    "if downstream scientific bottlenecks are removed.",
    "Amodei as canonical thinker: His previous essay 'The Adolescence of Technology' is already "
    "in the canon. This sequel adds the policy dimension — what should be built around the "
    "capability trajectory he described.",
]))
story.append(Spacer(1, 0.2*inch))
story.append(HRFlowable(color=MID_GRAY, thickness=0.5, spaceAfter=6))
story.append(Paragraph(
    "Source: darioamodei.com/post/policy-on-the-ai-exponential. Published June 10, 2026. "
    "Coverage drawn from: Bloomberg Law, SiliconAngle, VentureBeat, The Decoder, TechTimes, "
    "Business Standard, TechJuice, BeinCrypto, FourWeekMBA (June 10–15, 2026).",
    footer_style,
))

doc.build(story)
print("PDF created successfully.")
