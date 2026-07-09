import streamlit as st

from core.theme import inject_css
from core.views import render_home, render_resume, render_projects, render_contact

st.set_page_config(
    page_title="Ahmed Fouad — Portfolio",
    layout="wide",
)

inject_css()

tab_home, tab_resume, tab_projects, tab_contact = st.tabs(
    ["Home", "Resume", "Projects", "Contact"]
)

with tab_home:
    render_home()

with tab_resume:
    render_resume()

with tab_projects:
    render_projects()

with tab_contact:
    render_contact()
