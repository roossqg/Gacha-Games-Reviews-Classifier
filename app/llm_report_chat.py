#text -> process + output prompt -> model response
from ollama import chat
import pandas as pd
import json

import streamlit as st
from Models.rag_report import Gacha_Report

data = pd.read_csv('Gacha_Reviews/Datasets/wuwa_processed.csv')

def report_generate(data: pd.DataFrame,game: str) ->  json :

    #data = group_data(data)  --> extract features about each game
    data = data[data['game'] == game]

    while True:

        #msg = input('User: ')
        msg = f'game : {game}.give me a resume about the reviews of game history/lore'
        info = f'''Do it using the following reviews: {data['content'][:100].to_list()}'''

        example_output = {
    "game": "Generic Gacha Game Name",
    "resume": "A fantasy-themed gacha RPG where players recruit characters through a summoning (gacha) system to build teams and take on story-driven and event-based challenges.",
    "history": "The story follows the protagonist on a journey to restore balance to a fractured kingdom, gradually uncovering secrets about an ancient civilization and the powers behind the summonable characters.",
    "gameplay": "Turn-based or real-time combat, team building with elemental and class synergies, character progression through leveling, gear, and skills, plus PvE and PvP modes.",
    "characters": "A diverse cast of characters with different rarities (common, rare, epic, legendary), each featuring unique abilities, individual backstories, and distinct visuals that encourage collecting.",
    "events": "Limited-time events with exclusive rewards, featured summon banners, seasonal challenges, and crossover collaborations with other franchises.",
    "design": "Stylized anime-inspired art, immersive soundtrack, and an intuitive interface built for mobile devices.",
    "gacha": "Probability-based summoning system with premium and free currencies, a pity mechanic (guaranteed rare pull after X attempts), and rotating featured-character banners."
}



        prompts = [
                {'role': 'system',
                'content':'''You are a gacha reviews analyser which generate reports about each game.'''},

                #EXAMPLES
                {'role':'user','content':'generate a resume about the game.'},
                {'role':'assistant','content': json.dumps(example_output,indent=2)},

                {'role': 'user','content': msg + info}]

        
        response = chat(
            model='llama3.2:3b-instruct-q4_K_M',
            stream = False,
            messages=prompts,
            format=Gacha_Report.model_json_schema(),
            options={'temperature':0.3}
        )

        return (f'Bot: {response['message']['content']}')



#print(report_generate(data))