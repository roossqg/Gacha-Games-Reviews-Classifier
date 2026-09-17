import streamlit as st

page1 = st.Page(page='graphs.py',title='Text Graphs')
page2 = st.Page(page='ai_chat.py',title='Game Chatbot')
#page1 = st.Page(page='graphs.py',title='Text Graphs')
#page1 = st.Page(page='graphs.py',title='Text Graphs')


pg = st.navigation([page1],position='sidebar')

pg.run()