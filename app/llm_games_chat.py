#text -> process + output prompt -> model response

from ollama import chat
import pandas as pd

data = pd.read_csv('Gacha_Reviews/Datasets/wuwa_processed.csv')

def report_generate(data: pd.DataFrame):
    while True:

        #msg = input('User: ')
        msg = 'game : Wuthering Waves.give me a resume about the reviews of game history/lore'
        info = f'''Do it using the following reviews: {data['content'][:100].to_list()}'''
        
        response = chat(
            model='llama3.2:3b-instruct-q4_K_M',
            stream = False,
            messages=[
                {'role': 'system',
                'content':'You are a ai chatbot for feedback analyser that provides informations about gacha game reviews and customer behavior.'},
                {'role': 'user','content': msg + info}]
        )

        return (f'Bot: {response['message']['content']}')

print(report_generate(data))