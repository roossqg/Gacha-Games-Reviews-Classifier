import plotly.express as px
import matplotlib.pyplot as plt

import pandas as pd 

from app.data_handle.analyst import hist_tokens

def classify_sentiment_by_scores(data:pd.DataFrame):

    sentiment_labels =[]
    for i in range(0,len(data)):
        scores = {
        'POSITIVE': data.loc[i,'positive_score'],
        'NEGATIVE': data.loc[i,'negative_scores'],
        'NEUTRAL': data.loc[i,'neutral_scores']
        }

        sentiment_pred = max(scores,key=scores.get)
        #conf = max(scores.values())

       
        sentiment_labels.append(sentiment_pred)
       

    data['sentiment'] = sentiment_labels

    return data
        

def counts(data:pd.DataFrame):
    'counts sentiments'

    counts = data.groupby(['game','sentiment']).size().reset_index(name='counts')

    fig1 = px.bar(data_frame=counts,y='game',x='counts',color='sentiment',orientation='h')

    return fig1


def boxplot(data: pd.DataFrame):
    'scores distribution'

    fig1 = px.box(data_frame=data,y='positive_score',x='sentiment')
    fig2 = px.box(data_frame=data,y='negative_scores',x='sentiment')
    fig3 = px.box(data_frame=data,y='neutral_scores',x='sentiment')

    return {'fig1': fig1,'fig2': fig2,'fig3': fig3}

def histogram(data: pd.DataFrame):

    fig1 = px.histogram(data_frame=data[data['sentiment']=='POSITIVE'],x='positive_score')
    fig2 = px.histogram(data_frame=data[data['sentiment']=='NEGATIVE'],x='negative_scores')
    fig3 = px.histogram(data_frame=data[data['sentiment']=='NEUTRAL'],x='neutral_scores')

    return {'fig1': fig1,'fig2': fig2,'fig3': fig3}


def bar(data: pd.DataFrame):
    'most words-features per sentiment'

    data_pos = data[data['sentiment'] == 'POSITIVE']
    hist_tokens(data_pos)

    data_neg = data[data['sentiment'] == 'NEGATIVE']
    hist_tokens(data_neg)

    data_neu = data[data['sentiment'] == 'NEUTRAL']
    hist_tokens(data_neu)



