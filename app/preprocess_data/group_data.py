#separate data by history-gameplay-events-game-gacha-characters-design
from ollama import chat
import pandas as pd


#use llm to classify

def extract_game_features(data: pd.DataFrame) -> pd.DataFrame:

    classes = []
    for review in data['content']:

        messages = [
            {'role':'system','content':'''you are a gacha games review classifier'
            '' which categorize reviews using the categories:
            [gacha,history,events,charatecters,design,gameplay]'''},

            {'role':'user','content':'''know would realy improve 
            game skip buton many time repeatedly taping scren wanting get much
            dialog tolerate much patience run thin finished recent trailblaze mision
            tok longer imagined go helpful skip buton could
            all day every day even get started side companion misions'''},

            {'role':'assistant','content':'game'},

            {'role':'user','content': review}
        ]

        response = chat(
            model='llama3.2:3b-instruct-q4_K_M',
            stream = False,
            messages=messages

    )

        classes.append(response['message']['content'])

    data['classes'] = classes

    return data



