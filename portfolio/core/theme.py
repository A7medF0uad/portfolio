import streamlit as st

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;700&family=Inter:wght@400;500;600&display=swap');

:root {
    --bg-0: #0a0e14;
    --bg-1: #12181f;
    --bg-2: #1a222c;
    --accent-purple: #9d4edd;
    --accent-amber: #ffb703;
    --accent-green: #39ff9f;
    --text-0: #e6edf3;
    --text-1: #8b98a5;
    --border: #263140;
}

/* base */
.stApp {
    background-color: var(--bg-0);
    color: var(--text-0);
    font-family: 'Inter', sans-serif;
}

h1, h2, h3, h4, .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
    font-family: 'JetBrains Mono', monospace !important;
    color: var(--text-0);
    letter-spacing: -0.02em;
}

/* tab bar */
.stTabs [data-baseweb="tab-list"] {
    border-bottom: 1px solid var(--border);
}
.stTabs [data-baseweb="tab"] {
    font-family: 'JetBrains Mono', monospace;
    color: var(--text-1);
}
.stTabs [aria-selected="true"] {
    color: var(--accent-green) !important;
}

/* cards */
.term-card {
    background-color: var(--bg-1);
    border: 1px solid var(--border);
    border-radius: 6px;
    padding: 1.25rem 1.5rem;
    margin-bottom: 1rem;
}
.term-card:hover {
    border-color: var(--accent-purple);
}

/* prompt line */
.prompt {
    font-family: 'JetBrains Mono', monospace;
    color: var(--accent-green);
}
.prompt .path { color: var(--accent-purple); }
.prompt .cursor {
    display: inline-block;
    width: 8px; height: 1em;
    background: var(--accent-green);
    animation: blink 1s step-end infinite;
    vertical-align: text-bottom;
    margin-left: 2px;
}
@keyframes blink { 50% { opacity: 0; } }

/* tags/badges */
.tag {
    display: inline-block;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.75rem;
    color: var(--accent-amber);
    border: 1px solid var(--accent-amber);
    border-radius: 3px;
    padding: 0.1rem 0.5rem;
    margin: 0 0.35rem 0.35rem 0;
}

hr { border-color: var(--border); }

a { color: var(--accent-purple); }
a:hover { color: var(--accent-green); }

.muted { color: var(--text-1); }
</style>
"""


def inject_css() -> None:
    st.markdown(CSS, unsafe_allow_html=True)


def tag(text: str) -> str:
    return f'<span class="tag">{text}</span>'


def render_tags(items: list[str]) -> None:
    st.markdown("".join(tag(i) for i in items), unsafe_allow_html=True)
