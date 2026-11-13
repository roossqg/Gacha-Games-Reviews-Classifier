import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import streamlit as st


st.set_page_config(
    page_title="Gacha Review Insights",
    page_icon="🎮",
    layout="wide",
)

pages = [
    st.Page(
        page="report.py",
        title="Game Reports",
        icon="📝",
    ),
    st.Page(
        page="ai_chat.py",
        title="Game Assistant",
        icon="💬",
    ),
    st.Page(
        page="graphs.py",
        title="Explore Reviews",
        icon="📊",
    ),
    st.Page(
        page="sentiment_topics.py",
        title="Sentiment & Topics",
        icon="🧭",
    ),
    st.Page(
        page="evaluations.py",
        title="Evaluations & Tests",
        icon="🧪",
    ),
]

pg = st.navigation(pages, position="sidebar")
pg.run()