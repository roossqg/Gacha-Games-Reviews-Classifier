import streamlit as st
from ollama import chat
import pandas  as pd

from Models import rag_report
from llm_report_chat import report_generate

data = pd.read_csv('Gacha_Reviews\Datasets\wuwa_processed.csv')

def main():


    tab1,tab2,tab3,tab4,tab5 = st.tabs(['Genshin Impact','Honkai Star Rail',
                                        'Zenless Zone Zero','Wuthering Waves',
                                        'Blue Archive'])

    json_report_game1 = report_generate(data)

    json_report_game2 = report_generate(data)

    json_report_game3 = report_generate(data)

    json_report_game4 = report_generate(data)

    json_report_game5 = report_generate(data)






if __name__ == 'main':
    main()