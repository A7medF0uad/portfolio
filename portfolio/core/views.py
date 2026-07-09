"""
Render functions for each tab. Tabs (unlike st.Page/st.navigation) don't
support separate URLs, so all page content lives here as plain functions
and app.py just calls the right one inside each st.tabs() block.
"""

import base64
from pathlib import Path

import streamlit as st

from core.content import (
    NAME, HANDLE, LOCATION, TAGLINE, BIO, EMAIL, GITHUB, GITHUB_USER,
    SKILLS, RESUME_SECTIONS, PROJECTS,
)
from core.theme import prompt_line, render_tags, card_open, card_close

ASSETS_DIR = Path(__file__).resolve().parent.parent / "assets"
AVATAR_PATH = ASSETS_DIR / "me.png"


@st.cache_data
def _get_base64(path: Path) -> str:
    return base64.b64encode(path.read_bytes()).decode()


def render_home() -> None:
    prompt_line("~", "whoami")

    col_avatar, col_info = st.columns([1, 2])

    with col_avatar:
        if AVATAR_PATH.exists():
            img_b64 = _get_base64(AVATAR_PATH)
            st.markdown(
                f"""
                <style>
                .avatar {{
                    width: 180px;
                    height: 180px;
                    border-radius: 50%;
                    object-fit: cover;
                    border: 3px solid var(--accent-purple);
                }}
                </style>
                <img src="data:image/png;base64,{img_b64}" class="avatar">
                """,
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                "<span class='muted'>*(assets/me.png not found)*</span>",
                unsafe_allow_html=True,
            )

    with col_info:
        st.markdown(f"### {HANDLE}")
        st.markdown(f"<span class='muted'>{LOCATION}</span>", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown(f"## {NAME}")
    st.markdown(f"**{TAGLINE}**")
    st.write(BIO)


def render_resume() -> None:
    prompt_line("~", "cat resume.md")
    st.markdown("## Resume")

    st.markdown("### Skills")
    for category, items in SKILLS.items():
        st.markdown(f"**{category}**")
        render_tags(items)

    st.markdown("---")
    st.markdown("### Education")
    if RESUME_SECTIONS["education"]:
        for e in RESUME_SECTIONS["education"]:
            st.markdown(f"- {e}")
    else:
        st.markdown(
            "<span class='muted'>*(add degree, institution, expected graduation — TODO)*</span>",
            unsafe_allow_html=True,
        )

    st.markdown("### Certifications")
    if RESUME_SECTIONS["certifications"]:
        for c in RESUME_SECTIONS["certifications"]:
            st.markdown(f"- {c}")
    else:
        st.markdown(
            "<span class='muted'>*(add certifications here — TODO)*</span>",
            unsafe_allow_html=True,
        )

    st.markdown("### Experience")
    if RESUME_SECTIONS["experience"]:
        for x in RESUME_SECTIONS["experience"]:
            st.markdown(f"- {x}")
    else:
        st.markdown(
            "<span class='muted'>*(internships / work experience if any — TODO)*</span>",
            unsafe_allow_html=True,
        )


def _render_project_detail(p: dict) -> None:
    st.markdown(f"### {p['title']}")
    st.write(p["one_liner"])
    render_tags(p["stack"])

    st.markdown("---")
    st.markdown("**Overview**")
    st.write(p["details"])

    st.markdown("**Highlights**")
    for h in p["highlights"]:
        st.markdown(f"- {h}")

    st.markdown("---")
    links = []
    if p.get("github"):
        links.append(f"[View on GitHub]({p['github']})")
    if p.get("deployed_url"):
        links.append(f"[Live app]({p['deployed_url']})")
    if links:
        st.markdown(" &nbsp;|&nbsp; ".join(links))
    else:
        st.markdown(
            "<span class='muted'>*(GitHub link — TODO)*</span>",
            unsafe_allow_html=True,
        )


def render_projects() -> None:
    prompt_line("~/projects", "ls -la")
    st.markdown("## Projects")
    st.markdown(
        "<span class='muted'>Three projects, three different stacks — a from-scratch "
        "search algorithm, a statistical modeling dashboard, and a deployed ML app.</span>",
        unsafe_allow_html=True,
    )
    st.markdown("---")

    labels = [p["title"] for p in PROJECTS]
    sub_tabs = st.tabs(labels)
    for sub_tab, p in zip(sub_tabs, PROJECTS):
        with sub_tab:
            _render_project_detail(p)


def render_contact() -> None:
    prompt_line("~", "cat contact.md")
    st.markdown("## Contact")

    st.markdown(
        f"""
```
email    {EMAIL}
github   {GITHUB_USER}
handle   {HANDLE}
```
"""
    )

    st.markdown(f"[{EMAIL}](mailto:{EMAIL})")
    st.markdown(f"[{GITHUB}]({GITHUB})")

    st.markdown("---")
    st.markdown(
        "<span class='muted'>*(add LinkedIn profile link here if you want it "
        "listed too — TODO)*</span>",
        unsafe_allow_html=True,
    )
