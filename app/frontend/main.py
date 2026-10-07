import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import streamlit as st

page3 = st.Page(page='report.py',title='Game Reviews Resume Report')
page1 = st.Page(page='graphs.py',title='Text Graphs')
page2 = st.Page(page='ai_chat.py',title='Game Chatbot')
#page1 = st.Page(page='graphs.py',title='Text Graphs')


pg = st.navigation([page3,page2,page1],position='sidebar')

pg.run()