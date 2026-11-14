from wordcloud import WordCloud
#from huggingface_hub import pipeline 

import plotly.express as px
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

import streamlit as st

def count_tokens(serie:pd.Series):

    count = (serie.explode().value_counts().head(10).reset_index())
    count.columns =['token_sentence','count']

    return count


def hist_tokens(data: pd.DataFrame):

    df = count_tokens(data['word_token'])
    df2 = count_tokens(data['sentence_token'])

    right,left = st.columns(2)

    with right:
        fig = px.bar(df,y='token_sentence',x='count',title='Most frequent tokens',orientation='h')
        st.plotly_chart(fig)
    with left:
        fig2 = px.bar(df2,y='token_sentence',x='count',title='Most frequent sentences',orientation='h')
        st.plotly_chart(fig2)

    #data tokens -> sum vectors features


def reviews_length(data: pd.DataFrame) -> pd.DataFrame:

    data['word_length'] = data['word_token'].str.len()
    data['sentence_length'] = data['sentence_token'].str.len()
    data['content_length'] = data['content'].str.len()

    return data


def word_cloud(data: pd.DataFrame) -> dict:

    gacha_stop_words = ['game','games','history','characters','banner','gacha','events','update'
                             'gaming','play','player','players','mobile','phone','summon','summons','summoning',
                             'pull','pulls','pulling','roll','rolls','rolling','banners','spark','pity',
                             'rate','rates','drop','drops','graphic','meta','s','ss','star','stars','stats',
                             'stat','list','tier','level','lvl']

    full_text = " ".join(review for review in data['word_token'].dropna().astype(str))
    stopwords = set(ENGLISH_STOP_WORDS).union(set(gacha_stop_words))

    wc_with_stopwords = WordCloud(background_color='white',stopwords=stopwords).generate(
        full_text)
    wc_without_stopwords = WordCloud(background_color='white').generate(full_text)

    fig1,ax1 = plt.subplots()
    ax1.imshow(wc_with_stopwords,interpolation='bilinear')

    fig2,ax2 = plt.subplots()
    ax2.imshow(wc_without_stopwords,interpolation='bilinear')

    return {'fig1': fig1,'fig2': fig2}





    

