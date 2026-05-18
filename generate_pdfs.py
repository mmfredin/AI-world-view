"""
Generate PDFs for newly identified canonical AI perspective pieces.
"""
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY


def make_doc(filename, title, author, date, source_url, sections):
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        leftMargin=1.1 * inch,
        rightMargin=1.1 * inch,
        topMargin=1.1 * inch,
        bottomMargin=1.1 * inch,
    )

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        "Title",
        parent=styles["Normal"],
        fontSize=22,
        leading=28,
        spaceAfter=6,
        fontName="Helvetica-Bold",
        textColor=colors.HexColor("#1a1a2e"),
        alignment=TA_LEFT,
    )
    meta_style = ParagraphStyle(
        "Meta",
        parent=styles["Normal"],
        fontSize=11,
        leading=16,
        spaceAfter=4,
        fontName="Helvetica",
        textColor=colors.HexColor("#555555"),
    )
    url_style = ParagraphStyle(
        "URL",
        parent=styles["Normal"],
        fontSize=9,
        leading=13,
        spaceAfter=18,
        fontName="Helvetica",
        textColor=colors.HexColor("#2563eb"),
    )
    section_head_style = ParagraphStyle(
        "SectionHead",
        parent=styles["Normal"],
        fontSize=13,
        leading=18,
        spaceBefore=18,
        spaceAfter=6,
        fontName="Helvetica-Bold",
        textColor=colors.HexColor("#1a1a2e"),
    )
    body_style = ParagraphStyle(
        "Body",
        parent=styles["Normal"],
        fontSize=11,
        leading=17,
        spaceAfter=8,
        fontName="Helvetica",
        textColor=colors.HexColor("#1a1a1a"),
        alignment=TA_JUSTIFY,
    )
    quote_style = ParagraphStyle(
        "Quote",
        parent=styles["Normal"],
        fontSize=11,
        leading=17,
        spaceAfter=10,
        spaceBefore=6,
        fontName="Helvetica-Oblique",
        textColor=colors.HexColor("#2d2d2d"),
        leftIndent=24,
        rightIndent=24,
        borderPadding=(6, 6, 6, 6),
    )
    note_style = ParagraphStyle(
        "Note",
        parent=styles["Normal"],
        fontSize=9,
        leading=13,
        spaceAfter=6,
        fontName="Helvetica-Oblique",
        textColor=colors.HexColor("#888888"),
    )

    story = []

    story.append(Paragraph(title, title_style))
    story.append(Paragraph(f"{author} &nbsp;&nbsp;|&nbsp;&nbsp; {date}", meta_style))
    story.append(Paragraph(source_url, url_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#1a1a2e")))
    story.append(Spacer(1, 12))

    for section in sections:
        kind = section.get("type", "body")
        text = section.get("text", "")
        if kind == "section":
            story.append(Paragraph(text, section_head_style))
        elif kind == "quote":
            story.append(Paragraph(f'&#8220;{text}&#8221;', quote_style))
        elif kind == "note":
            story.append(Paragraph(text, note_style))
        elif kind == "spacer":
            story.append(Spacer(1, int(text)))
        else:
            story.append(Paragraph(text, body_style))

    doc.build(story)
    print(f"Created: {filename}")


# ─── PDF 1: Sam Altman — Reflections ─────────────────────────────────────────

altman_reflections_sections = [
    {
        "type": "note",
        "text": (
            "Source: blog.samaltman.com/reflections — Published April 13, 2026. "
            "This document reproduces the key content and verbatim quotes from Sam Altman's "
            "'Reflections' essay, compiled from the original post and published analyses."
        ),
    },
    {
        "type": "section",
        "text": "Overview",
    },
    {
        "type": "body",
        "text": (
            "Published on April 13, 2026, 'Reflections' is Sam Altman's retrospective on OpenAI's "
            "nearly nine-year journey and a forward declaration about the path to superintelligence. "
            "Written at what Altman calls an inflection point — as the company approaches AGI — the "
            "essay is notable for two things: a confident, unequivocal statement that OpenAI now "
            "knows how to build AGI, and an explicit pivot in strategic ambition toward "
            "superintelligence as the next target."
        ),
    },
    {
        "type": "section",
        "text": "The AGI Declaration",
    },
    {
        "type": "body",
        "text": (
            "The essay opens with Altman acknowledging that OpenAI started almost nine years ago "
            "because they believed AGI was possible and that it could be the most impactful "
            "technology in human history. After years of uncertainty, the company's posture has "
            "changed decisively:"
        ),
    },
    {
        "type": "quote",
        "text": (
            "We are now confident we know how to build AGI as we have traditionally understood it."
        ),
    },
    {
        "type": "body",
        "text": (
            "This is a significant escalation from OpenAI's earlier hedged language. The claim is "
            "not that AGI has been achieved, but that the path to it is understood — which, in "
            "Altman's framing, means the outcome is inevitable rather than uncertain. The emphasis "
            "is on the change in epistemic state: from 'we believe it's possible' to 'we know how.'"
        ),
    },
    {
        "type": "section",
        "text": "The Pivot to Superintelligence",
    },
    {
        "type": "body",
        "text": (
            "Having declared confidence on AGI, Altman immediately sets a higher ambition:"
        ),
    },
    {
        "type": "quote",
        "text": (
            "We are beginning to turn our aim beyond that, to superintelligence in the true sense "
            "of the word. We love our current products, but we are here for the glorious future. "
            "With superintelligence, we can do anything else."
        ),
    },
    {
        "type": "body",
        "text": (
            "The phrase 'We can do anything else' signals a belief that superintelligence is not "
            "just another milestone but a singularly enabling achievement — that once reached, "
            "other problems become tractable. This frames every current product and capability as "
            "instrumental toward the ultimate goal."
        ),
    },
    {
        "type": "section",
        "text": "The Promise of Superintelligent Tools",
    },
    {
        "type": "quote",
        "text": (
            "Superintelligent tools could massively accelerate scientific discovery and innovation "
            "well beyond what we are capable of doing on our own, and in turn massively increase "
            "abundance and prosperity."
        ),
    },
    {
        "type": "body",
        "text": (
            "Altman's vision for superintelligence is fundamentally about access and abundance. "
            "He argues for making superintelligence cheap, widely available, and not too "
            "concentrated with any person, company, or country. This is a notable stance for "
            "the CEO of one of the world's most powerful AI companies — one that frames the "
            "company's mission in terms of distribution rather than capture."
        ),
    },
    {
        "type": "section",
        "text": "The Event Horizon",
    },
    {
        "type": "quote",
        "text": "We are past the event horizon; the takeoff has started.",
    },
    {
        "type": "body",
        "text": (
            "This is perhaps the essay's most consequential claim. An event horizon in physics is "
            "the point of no return past a black hole — beyond which outcomes are determined by "
            "momentum rather than choice. Altman is asserting that AI's trajectory is now set, "
            "and the remaining question is how the world adapts to what is already underway."
        ),
    },
    {
        "type": "section",
        "text": "A Near-Term Timeline",
    },
    {
        "type": "body",
        "text": (
            "Consistent with his earlier essays, Altman lays out a near-term timeline that is "
            "compressed and concrete:"
        ),
    },
    {
        "type": "body",
        "text": (
            "<b>2025:</b> The arrival of agents that can do real cognitive work. Writing computer "
            "code will never be the same."
        ),
    },
    {
        "type": "body",
        "text": (
            "<b>2026:</b> The likely arrival of systems that can figure out novel insights — "
            "AI that doesn't just process existing knowledge but generates genuinely new ones."
        ),
    },
    {
        "type": "body",
        "text": (
            "<b>2027:</b> The potential arrival of robots that can do tasks in the real world, "
            "extending AI from the digital to the physical domain."
        ),
    },
    {
        "type": "section",
        "text": "On Pace and Organizational Learning",
    },
    {
        "type": "quote",
        "text": "The last two years have been like a decade at a normal company.",
    },
    {
        "type": "body",
        "text": (
            "Altman's description of OpenAI's pace is not just corporate boasting — it is a "
            "signal about how differently AI-native organizations experience time. The implication "
            "for non-AI-native institutions is significant: if the last two years felt like a decade "
            "inside OpenAI, then organizations operating at a normal pace have already fallen far "
            "further behind than they realize. The gap is not linear."
        ),
    },
    {
        "type": "section",
        "text": "On Safety and Distribution",
    },
    {
        "type": "quote",
        "text": (
            "We're pretty confident that in the next few years, everyone will see what we see, "
            "and that the need to act with great care, while still maximizing broad benefit and "
            "empowerment, is so important."
        ),
    },
    {
        "type": "body",
        "text": (
            "Altman does not treat the safety question as resolved. Rather, he expresses confidence "
            "that the importance of careful action will become self-evident to a broader audience. "
            "The framing is paternalistic in the best sense: not 'trust us, it's fine,' but 'you "
            "will come to see what we see.' It positions OpenAI as ahead of public understanding, "
            "with an implied obligation to lead carefully during that gap."
        ),
    },
    {
        "type": "section",
        "text": "Why This Essay Matters for the AI Worldview",
    },
    {
        "type": "body",
        "text": (
            "Three things distinguish 'Reflections' from Altman's earlier writing and make it "
            "worth incorporating into the canon:"
        ),
    },
    {
        "type": "body",
        "text": (
            "<b>1. The shift from 'possible' to 'known.'</b> Every prior statement from OpenAI "
            "hedged on whether AGI was achievable on a near-term timeline. This essay removes "
            "that hedge. If Altman is correct, the debate about AGI timing is essentially settled "
            "inside the company most likely to build it first."
        ),
    },
    {
        "type": "body",
        "text": (
            "<b>2. The explicit pivot toward superintelligence.</b> The strategic target has moved. "
            "AGI is now an intermediate milestone, not the destination. This changes the frame "
            "for what investments, timelines, and governance structures are relevant."
        ),
    },
    {
        "type": "body",
        "text": (
            "<b>3. The 'event horizon' framing.</b> This is the most operationally significant "
            "claim. If the trajectory is already set — if we are past the point of no return — "
            "then the strategic question for every organization is no longer 'whether' but "
            "'how fast' and 'how to position.' The argument for deliberate preparation, rather "
            "than wait-and-see, becomes much harder to rebut."
        ),
    },
]

make_doc(
    "/home/user/AI-world-view/Reflections - Sam Altman.pdf",
    "Reflections",
    "Sam Altman",
    "April 13, 2026",
    "https://blog.samaltman.com/reflections",
    altman_reflections_sections,
)


# ─── PDF 2: Andrej Karpathy — Sequoia AI Ascent 2026 ─────────────────────────

karpathy_sections = [
    {
        "type": "note",
        "text": (
            "Source: karpathy.bearblog.dev/sequoia-ascent-2026 — May 2026. "
            "This document reproduces the key content and verbatim quotes from Andrej Karpathy's "
            "post-talk summary of his fireside chat at Sequoia AI Ascent 2026, "
            "compiled from the original blog post and published analyses."
        ),
    },
    {
        "type": "section",
        "text": "Overview",
    },
    {
        "type": "body",
        "text": (
            "In May 2026, Andrej Karpathy (co-founder of OpenAI, former head of AI at Tesla, "
            "founder of Eureka Labs) spoke at Sequoia's AI Ascent conference with partner "
            "Stephanie Zhan. In a characteristically pithy move, Karpathy fed an LLM all of "
            "his recent blog posts and tweets, had it read the video transcript, and used that "
            "to generate a cleaned-up summary — which he then published as his 'Sequoia Ascent "
            "2026' blog post. The talk introduces a three-era framework for software development "
            "and marks a critical distinction that has significant implications for how "
            "organizations build with AI."
        ),
    },
    {
        "type": "section",
        "text": "The Software Evolution Framework: 1.0 → 2.0 → 3.0",
    },
    {
        "type": "body",
        "text": (
            "Karpathy organizes the history of software development into three eras, each defined "
            "by how humans program computers:"
        ),
    },
    {
        "type": "body",
        "text": (
            "<b>Software 1.0:</b> Humans write explicit rules in code. Logic, "
            "conditionals, algorithms. The programmer specifies exactly what the computer "
            "should do in every situation."
        ),
    },
    {
        "type": "body",
        "text": (
            "<b>Software 2.0:</b> Humans curate datasets and train neural networks. "
            "The programmer specifies the objective and provides examples; the machine "
            "learns the rules from data. This is the era of deep learning."
        ),
    },
    {
        "type": "body",
        "text": (
            "<b>Software 3.0:</b> Humans program LLMs through prompts, context, tools, "
            "examples, memory, and instructions. The 'program' is a paragraph in a context "
            "window rather than a function in a file. The LLM is the interpreter."
        ),
    },
    {
        "type": "section",
        "text": "The Defining Insight: Specify vs. Verify",
    },
    {
        "type": "body",
        "text": (
            "Karpathy's most important and quotable claim from the talk:"
        ),
    },
    {
        "type": "quote",
        "text": (
            "Traditional computers automate what you can specify in code. "
            "This latest round of LLMs can automate what you can verify."
        ),
    },
    {
        "type": "body",
        "text": (
            "This distinction is deceptively profound. Specification requires complete, "
            "unambiguous knowledge of the procedure. Verification requires only the ability to "
            "judge whether an output is correct — a much lower bar. Almost everything humans "
            "know how to judge but can't fully articulate is now potentially automatable. "
            "This redraws the boundary between human and machine work in a way that is "
            "significantly more expansive than previous conceptions."
        ),
    },
    {
        "type": "section",
        "text": "The Context Window as the New Programming Surface",
    },
    {
        "type": "body",
        "text": (
            "In Software 3.0, the primary unit of programming is no longer the function — "
            "it is the context window. The LLM performs computation over the information "
            "placed in that context. This means:"
        ),
    },
    {
        "type": "body",
        "text": (
            "The main lever is what goes into the context window: instructions, examples, "
            "memory, tool outputs, and domain knowledge. Quality of context determines quality "
            "of output. This directly validates the worldview's emphasis on context engineering "
            "as the essential competitive differentiator."
        ),
    },
    {
        "type": "body",
        "text": (
            "Infrastructure must become agent-native, not user-native. Most software today "
            "was designed for humans clicking buttons and reading docs. The next wave of "
            "infrastructure will be built for agents that read, act, and iterate — "
            "a fundamental redesign of the interface layer."
        ),
    },
    {
        "type": "section",
        "text": "Vibe Coding vs. Agentic Engineering",
    },
    {
        "type": "body",
        "text": (
            "Karpathy draws a critical distinction between two modes of AI-assisted building:"
        ),
    },
    {
        "type": "body",
        "text": (
            "<b>Vibe coding</b> is when anyone builds software by describing what they want. "
            "A non-technical person creates apps, websites, tools, automations, prototypes, "
            "and internal systems by prompting an AI. It raises the floor dramatically — "
            "the barrier to creating functional software has collapsed."
        ),
    },
    {
        "type": "body",
        "text": (
            "<b>Agentic engineering</b> is what professional builders do in Software 3.0. "
            "It means using AI agents to accomplish complex, multi-step technical tasks while "
            "preserving professional quality and maintaining understanding of what is being built. "
            "It raises the ceiling for what professionals can accomplish."
        ),
    },
    {
        "type": "quote",
        "text": (
            "Vibe coding raises the floor. Agentic engineering raises the ceiling. "
            "Both matter, and they are not the same thing."
        ),
    },
    {
        "type": "section",
        "text": "December 2025: The Inflection Point",
    },
    {
        "type": "body",
        "text": (
            "Karpathy identifies December 2025 as the moment when agentic coding tools "
            "crossed a qualitative threshold:"
        ),
    },
    {
        "type": "quote",
        "text": (
            "You really had to look again as of December, because things changed fundamentally, "
            "especially in this agentic, coherent workflow. It really started to work."
        ),
    },
    {
        "type": "body",
        "text": (
            "Before December 2025, coding agents were helpful but inconsistent — they "
            "produced messy output that required significant human correction. After that "
            "point, they started producing large chunks of correct, production-quality code "
            "reliably. Karpathy himself stopped writing code manually after December, "
            "delegating entirely to agents. This is not a future prediction — it is a "
            "description of what has already occurred."
        ),
    },
    {
        "type": "section",
        "text": "The 'Ghost' Problem and What Can't Be Outsourced",
    },
    {
        "type": "body",
        "text": (
            "Karpathy introduces the concept of AI agents as 'ghosts' — they operate in "
            "the environment, they take actions, but their internal state and reasoning "
            "are not fully transparent. This creates a new professional requirement: "
            "mastering ghost management."
        ),
    },
    {
        "type": "body",
        "text": (
            "This leads to what may be the talk's most important practical warning:"
        ),
    },
    {
        "type": "quote",
        "text": "You can outsource thinking. You can't outsource understanding.",
    },
    {
        "type": "body",
        "text": (
            "The professional who uses agentic tools to their full potential while retaining "
            "deep understanding of the domain and the system is the one who wins. "
            "The professional who delegates thinking entirely and loses the ability to verify "
            "is the one who gets replaced — not by AI, but by a human who uses AI better."
        ),
    },
    {
        "type": "section",
        "text": "Implications for the AI Worldview",
    },
    {
        "type": "body",
        "text": (
            "Karpathy's talk at Sequoia AI Ascent 2026 advances the worldview on several fronts:"
        ),
    },
    {
        "type": "body",
        "text": (
            "<b>1. Validates the context engineering thesis.</b> The Software 3.0 framework "
            "is the technical foundation for why context engineering matters. If the context "
            "window is the program and the LLM is the interpreter, then whoever constructs "
            "the best context wins. Domain experts who understand what belongs in that context "
            "are the scarce resource."
        ),
    },
    {
        "type": "body",
        "text": (
            "<b>2. Reframes the agentic AI inflection point.</b> December 2025 is not "
            "a prediction but a documented past event. The agentic wave the worldview "
            "identifies as '2025-2026 inflection' has already landed. The question for "
            "organizations is no longer 'when will agents work?' but 'how do we operate now "
            "that they do?'"
        ),
    },
    {
        "type": "body",
        "text": (
            "<b>3. Provides the 'specify vs. verify' frame.</b> This is the clearest "
            "articulation of why AI's scope is larger than previous waves of automation. "
            "Automation has historically been limited to what humans could fully specify. "
            "The new boundary is verification — and almost every knowledge worker can verify "
            "outputs in their domain without fully being able to specify the procedure."
        ),
    },
    {
        "type": "body",
        "text": (
            "<b>4. Grounds the 'You can't outsource understanding' imperative.</b> "
            "This is the most direct statement yet of why deep domain expertise remains "
            "essential even as AI handles the execution. It is the strongest counter-argument "
            "to blanket AI replacement fears and the clearest statement of what humans must "
            "retain to remain irreplaceable."
        ),
    },
    {
        "type": "body",
        "text": (
            "<b>5. Signals infrastructure redesign ahead.</b> The shift to agent-native "
            "infrastructure is not yet complete. The next wave of value creation — "
            "for vendors, for banks, for anyone building on AI — will come from rebuilding "
            "systems designed for agents rather than bolting AI onto systems designed for humans."
        ),
    },
]

make_doc(
    "/home/user/AI-world-view/Sequoia AI Ascent 2026 - Andrej Karpathy.pdf",
    "Sequoia AI Ascent 2026: Software 3.0 and the Rise of Agentic Engineering",
    "Andrej Karpathy",
    "May 2026",
    "https://karpathy.bearblog.dev/sequoia-ascent-2026/",
    karpathy_sections,
)
