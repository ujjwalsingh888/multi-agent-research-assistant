"""
Streamlit UI for the multi-agent research pipeline (pipeline.py).

Run with:
    streamlit run app.py

This file must live in the SAME folder as pipeline.py, agents.py and tools.py
so that `from agents import ...` works.
"""

import streamlit as st

st.set_page_config(page_title="ResearchMind", page_icon="🧭", layout="wide")

# ----------------------------------------------------------------------------
# Theme
# ----------------------------------------------------------------------------
ACCENT = "#ff7a3d"
ACCENT_SOFT = "#ffa869"
BG = "#0b0b0d"
PANEL = "#151517"
PANEL_BORDER = "#26262a"
TEXT = "#f2f0eb"
TEXT_DIM = "#8a8a8f"

st.markdown(f"""
<style>
    #MainMenu, footer, header {{ visibility: hidden; }}
    .stApp {{
        background: radial-gradient(circle at 20% 0%, #17130f 0%, {BG} 45%);
        color: {TEXT};
        font-family: 'Helvetica Neue', Arial, sans-serif;
    }}
    .block-container {{ padding-top: 3rem; max-width: 1150px; }}

    .eyebrow {{
        color: {ACCENT};
        font-size: 0.78rem;
        letter-spacing: 0.18em;
        font-weight: 600;
        margin-bottom: 0.6rem;
    }}
    .hero-title {{
        font-size: 3.4rem;
        font-weight: 800;
        line-height: 1.05;
        margin: 0 0 1rem 0;
        letter-spacing: -0.02em;
    }}
    .hero-title span {{ color: {ACCENT}; }}
    .hero-sub {{
        color: {TEXT_DIM};
        font-size: 1.05rem;
        max-width: 560px;
        line-height: 1.5;
        margin-bottom: 2.2rem;
    }}

    .panel {{
        background: {PANEL};
        border: 1px solid {PANEL_BORDER};
        border-radius: 14px;
        padding: 1.4rem 1.5rem;
    }}

    .step-card {{
        background: {PANEL};
        border: 1px solid {PANEL_BORDER};
        border-radius: 12px;
        padding: 0.95rem 1.1rem;
        margin-bottom: 0.7rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
        transition: border-color 0.2s ease;
    }}
    .step-card.active {{ border-color: {ACCENT}; }}
    .step-card.done {{ border-color: #3d5c3d; }}
    .step-name {{ font-weight: 600; font-size: 0.98rem; margin-bottom: 0.15rem; }}
    .step-desc {{ color: {TEXT_DIM}; font-size: 0.82rem; }}
    .step-num {{
        color: {ACCENT};
        font-size: 0.75rem;
        font-weight: 700;
        letter-spacing: 0.05em;
        margin-right: 0.6rem;
    }}
    .status-badge {{
        font-size: 0.68rem;
        letter-spacing: 0.06em;
        font-weight: 700;
        padding: 0.22rem 0.55rem;
        border-radius: 20px;
        white-space: nowrap;
    }}
    .status-waiting {{ color: {TEXT_DIM}; background: #1e1e21; }}
    .status-active {{ color: {BG}; background: {ACCENT}; }}
    .status-done {{ color: #b7e3b7; background: #1c2b1c; }}
    .status-error {{ color: #f2b3b3; background: #2b1c1c; }}

    div[data-testid="stTextInput"] input {{
        background: {PANEL} !important;
        border: 1px solid {PANEL_BORDER} !important;
        color: {TEXT} !important;
        border-radius: 10px !important;
        padding: 0.7rem 0.9rem !important;
    }}
    div[data-testid="stTextInput"] label {{
        color: {TEXT_DIM} !important;
        font-size: 0.78rem !important;
        letter-spacing: 0.08em;
        font-weight: 600;
    }}

    div.stButton > button {{
        background: linear-gradient(90deg, {ACCENT} 0%, {ACCENT_SOFT} 100%) !important;
        color: #1a0f08 !important;
        border: none !important;
        border-radius: 10px !important;
        font-weight: 700 !important;
        padding: 0.7rem 1rem !important;
        width: 100%;
    }}
    div.stButton > button:hover {{ filter: brightness(1.06); }}

    .panel-heading {{
        font-size: 1.05rem;
        font-weight: 700;
        margin-bottom: 1rem;
    }}

    .stTabs [data-baseweb="tab"] {{ color: {TEXT_DIM}; }}
    .stTabs [aria-selected="true"] {{ color: {ACCENT} !important; }}
</style>
""", unsafe_allow_html=True)

# ----------------------------------------------------------------------------
# Hero
# ----------------------------------------------------------------------------
st.markdown('<div class="eyebrow">MULTI-AGENT AI SYSTEM</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-title">Research<span>Mind</span></div>', unsafe_allow_html=True)
st.markdown(
    '<div class="hero-sub">Four specialized AI agents collaborate — searching, scraping, '
    'writing, and critiquing — to deliver a polished research report on any topic.</div>',
    unsafe_allow_html=True,
)

# ----------------------------------------------------------------------------
# State
# ----------------------------------------------------------------------------
STEPS = [
    ("01", "Search Agent", "Gathers recent web information"),
    ("02", "Reader Agent", "Scrapes & extracts deep content"),
    ("03", "Writer Chain", "Drafts the research report"),
    ("04", "Critic Chain", "Reviews and refines the report"),
]

if "result" not in st.session_state:
    st.session_state.result = None
if "step_status" not in st.session_state:
    st.session_state.step_status = ["waiting"] * 4

def render_steps(placeholder):
    labels = {"waiting": "WAITING", "active": "RUNNING", "done": "DONE", "error": "FAILED"}
    html = ""
    for (num, name, desc), status in zip(STEPS, st.session_state.step_status):
        card_class = "active" if status == "active" else ("done" if status == "done" else "")
        html += f"""
        <div class="step-card {card_class}">
            <div>
                <div class="step-name"><span class="step-num">{num}</span>{name}</div>
                <div class="step-desc">{desc}</div>
            </div>
            <div class="status-badge status-{status}">{labels[status]}</div>
        </div>
        """
    placeholder.markdown(html, unsafe_allow_html=True)

# ----------------------------------------------------------------------------
# Layout
# ----------------------------------------------------------------------------
left, right = st.columns([1.3, 1], gap="large")

with left:
    st.markdown('<div class="panel">', unsafe_allow_html=True)
    topic = st.text_input("RESEARCH TOPIC", placeholder="e.g. Quantum computing breakthroughs in 2025")
    run_clicked = st.button("⚡ Run Research Pipeline")
    st.markdown('</div>', unsafe_allow_html=True)

with right:
    st.markdown('<div class="panel-heading">Pipeline</div>', unsafe_allow_html=True)
    steps_placeholder = st.empty()
    render_steps(steps_placeholder)

# ----------------------------------------------------------------------------
# Run pipeline
# ----------------------------------------------------------------------------
if run_clicked:
    if not topic.strip():
        st.warning("Please enter a topic first.")
    else:
        st.session_state.step_status = ["waiting"] * 4
        state = {}
        try:
            from agents import build_reader_agent, build_search_agent, writer_chain, critic_chain

            # Step 1 - search agent
            st.session_state.step_status[0] = "active"
            render_steps(steps_placeholder)
            search_agent = build_search_agent()
            search_result = search_agent.invoke({
                "messages": [("user", f"Find recent, reliable and detailed information about: {topic}")]
            })
            state["search_results"] = search_result["messages"][-1].content
            st.session_state.step_status[0] = "done"
            render_steps(steps_placeholder)

            # Step 2 - reader agent
            st.session_state.step_status[1] = "active"
            render_steps(steps_placeholder)
            reader_agent = build_reader_agent()
            reader_result = reader_agent.invoke({
                "messages": [("user",
                    f"Based on the following search results about '{topic}', "
                    f"pick the most relevant URL and scrape it for deeper content.\n\n"
                    f"Search Results:\n{state['search_results'][:800]}"
                )]
            })
            state["scraped_content"] = reader_result["messages"][-1].content
            st.session_state.step_status[1] = "done"
            render_steps(steps_placeholder)

            # Step 3 - writer chain
            st.session_state.step_status[2] = "active"
            render_steps(steps_placeholder)
            research_combined = (
                f"SEARCH RESULTS : \n {state['search_results']} \n\n"
                f"DETAILED SCRAPED CONTENT : \n {state['scraped_content']}"
            )
            state["report"] = writer_chain.invoke({"topic": topic, "research": research_combined})
            st.session_state.step_status[2] = "done"
            render_steps(steps_placeholder)

            # Step 4 - critic chain
            st.session_state.step_status[3] = "active"
            render_steps(steps_placeholder)
            state["feedback"] = critic_chain.invoke({"report": state["report"]})
            st.session_state.step_status[3] = "done"
            render_steps(steps_placeholder)

            st.session_state.result = state

        except Exception as e:
            idx = st.session_state.step_status.index("active") if "active" in st.session_state.step_status else 0
            st.session_state.step_status[idx] = "error"
            render_steps(steps_placeholder)
            st.error(f"Pipeline failed: {e}")

# ----------------------------------------------------------------------------
# Results
# ----------------------------------------------------------------------------
state = st.session_state.result
if state:
    def as_text(x):
        return getattr(x, "content", x)

    st.write("")
    st.markdown('<div class="panel-heading">Results</div>', unsafe_allow_html=True)
    report_tab, feedback_tab, sources_tab = st.tabs(["📄 Report", "🧐 Critic Feedback", "🗂 Raw Sources"])

    with report_tab:
        st.markdown(as_text(state["report"]))
        st.download_button(
            "Download report (.md)",
            data=str(as_text(state["report"])),
            file_name="research_report.md",
            mime="text/markdown",
        )

    with feedback_tab:
        st.markdown(as_text(state["feedback"]))

    with sources_tab:
        with st.expander("Search results", expanded=False):
            st.write(state["search_results"])
        with st.expander("Scraped content", expanded=False):
            st.write(state["scraped_content"])