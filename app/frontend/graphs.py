import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st
from preprocess_data.load import load_data
from preprocess_data.preprocess import clean_text_data,semantic_meaning,Word_Vector
from preprocess_data.group_data import extract_game_features

from analyst import word_cloud,hist_tokens,reviews_length

import pandas as pd
import plotly.express as px

def words_meaning():
    #data = load_data()
    data = clean_text_data()
    data = semantic_meaning(data)
    data2 = Word_Vector(data)

    return data

def game_graph(results: pd.DataFrame,game: str):

        results_game = results[results['game'] == game]

        left_col,right_col = st.colums(2)
        with left_col:
            st.pyplot(results_game['fig1'])
        with right_col:
            st.pyplot(results_game['fig2'])

def main():
    data = words_meaning()
    data = extract_game_features(data)

    col1,col2 = st.columns(2)

    #TOTAL
    results_word_cloud = word_cloud(data)

    with col1:
        st.pyplot(results_word_cloud['fig1'])

    with col2:
        st.pyplot(results_word_cloud['fig2'])

    games =  ['Genshin Impact','Honkai Star Rail','Zenless Zone Zero',
            'Wuthering Waves','Blue Archive']

    #BY GAME 

    for game in games:
        game_graph(results_word_cloud,game=game)


    st.divider()

    results_count_tokens = hist_tokens(data)
    col4,col5 = st.columns(2)

    with col4:
        st.pyplot(results_count_tokens['fig'])

    with col5:
        st.pyplot(results_count_tokens['fig2'])


    #BY GAME    

    for game in games:
        game_graph(results_count_tokens,game=game)


    lengths = reviews_length(data)

    col_len1,col_len2 = st.columns(2)

    col_len1.metric('Word Mean Length ',lengths['word_length'].mean())
    col_len2.metirc('Sentence Mean Length ',lengths['sentence_length'].mean())

    box1 = px.box(lengths,x='game',y='word_length')
    box2 = px.box(lengths,x='game',y='sentence_length')

    st.plotly_chart(box1)
    st.plotly_chart(box2)

    df = features_weighted = Word_Vector(method='tfidf')
    st.dataframe(df.head(5))

    df_count = df.sum(axis=0)

    fig1 = px.histogram(df_count)

    st.plotly_chart(fig1)

if __name__ == '__main__':
    main()
