import plotly.express as px
import matplotlib.pyplot as plt

import pandas as pd 
import streamlit as st

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

    fig1 = px.bar(
        data_frame=counts,
        y='game',
        x='counts',
        color='sentiment',
        orientation='h',
        title='Review counts by game and sentiment',
        labels={'game': 'Game', 'counts': 'Reviews', 'sentiment': 'Sentiment'},
        category_orders={'sentiment': ['POSITIVE', 'NEUTRAL', 'NEGATIVE']},
    )

    return fig1


def boxplot(data: pd.DataFrame):
    'scores distribution'

    fig1 = px.box(
        data_frame=data,
        y='positive_score',
        x='sentiment',
        title='Positive score distribution',
        labels={'positive_score': 'Positive score', 'sentiment': 'Sentiment'},
    )
    fig2 = px.box(
        data_frame=data,
        y='negative_scores',
        x='sentiment',
        title='Negative score distribution',
        labels={'negative_scores': 'Negative score', 'sentiment': 'Sentiment'},
    )
    fig3 = px.box(
        data_frame=data,
        y='neutral_scores',
        x='sentiment',
        title='Neutral score distribution',
        labels={'neutral_scores': 'Neutral score', 'sentiment': 'Sentiment'},
    )

    return {'fig1': fig1,'fig2': fig2,'fig3': fig3}

def histogram(data: pd.DataFrame):

    fig1 = px.histogram(
        data_frame=data[data['sentiment']=='POSITIVE'],
        x='positive_score',
        title='Positive sentiment scores',
        labels={'positive_score': 'Positive score'},
    )
    fig2 = px.histogram(
        data_frame=data[data['sentiment']=='NEGATIVE'],
        x='negative_scores',
        title='Negative sentiment scores',
        labels={'negative_scores': 'Negative score'},
    )
    fig3 = px.histogram(
        data_frame=data[data['sentiment']=='NEUTRAL'],
        x='neutral_scores',
        title='Neutral sentiment scores',
        labels={'neutral_scores': 'Neutral score'},
    )

    return {'fig1': fig1,'fig2': fig2,'fig3': fig3}


def bar(data: pd.DataFrame):
    'most words-features per sentiment'

    sentiment_groups = [
        ('POSITIVE', '😊 Positive reviews'),
        ('NEGATIVE', '😞 Negative reviews'),
        ('NEUTRAL', '😐 Neutral reviews'),
    ]
    for sentiment, title in sentiment_groups:
        st.markdown(f'##### {title}')
        hist_tokens(data[data['sentiment'] == sentiment])



