import plotly.express as px
import matplotlib.pyplot as plt

import pandas as pd 

def classify_sentiment_by_scores(data):

    sentiment_labels =[]
    for review,i in enumerate(0,len(data)):
        scores = {
        'POSITIVE': data[i,'positive_score'],
        'NEGATIVE': data[i,'negative_scores'],
        'NEUTRAL': data[i,'neutral_scores']
        }

        sentiment_pred = max(scores,key=scores.get)
        conf = max(scores.values())

        if conf >= 0.5:
            sentiment_labels.append(sentiment_pred)
        else:
            sentiment_labels.append('UNCERTAIN')


    data['sentiment'] = sentiment_labels

    return data
        

def counts(data:pd.DataFrame):
    'counts sentiments'

    counts = data.groupby(['game'])['sentiment'].count().reset_index(name='counts')

    px.bar(data=counts,x='game',color='sentiment')

    



def boxplot():
    'scores distribution'

def bar():
    'most words-features per sentiment'

