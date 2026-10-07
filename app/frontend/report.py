import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import json

import pandas as pd
import streamlit as st

from llm_report_chat import report_generate
from preprocess_data.load import load_data

data = load_data()


def render_game_tab(tab, game_name, display_name):
    with tab:
        report_raw = report_generate(data, game=game_name)
        report_data = json.loads(report_raw.removeprefix('Bot: '))

        st.subheader(display_name)
        st.badge('Resume', color='yellow')
        left_col, right_col = st.columns(2)

        left_col.badge('History', color='green')
        left_col.write(report_data['history'])

        left_col.badge('Gameplay', color='blue')
        left_col.write(report_data['gameplay'])

        left_col.badge('Design', color='violet')
        left_col.write(report_data['design'])

        right_col.badge('Characters', color='red')
        right_col.write(report_data['characters'])

        right_col.badge('Events', color='gray')
        right_col.write(report_data['events'])

        right_col.badge('Gacha', color='orange')
        right_col.write(report_data['gacha'])


def main():
    game_tabs = [
        ('Genshin Impact', 'Genshin Impact'),
        ('Honkai Star Rail', 'Honkai: Star Rail'),
        ('Zenless Zone Zero', 'Zenless Zone Zero'),
        ('Wuthering Waves', 'Wuthering Waves'),
        ('Blue Archive', 'Blue Archive'),
    ]

    tabs = st.tabs([name for _, name in game_tabs])

    for tab, (game_name, display_name) in zip(tabs, game_tabs):
        render_game_tab(tab, game_name, display_name)


if __name__ == '__main__':
    main()