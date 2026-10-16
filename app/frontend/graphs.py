import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st
from preprocess_data.load import load_data
from preprocess_data.preprocess import remove_stop_words,tokenize,semantic_meaning,Word_Vector
from preprocess_data.group_data import extract_game_features

from analyst import word_cloud,hist_tokens,reviews_length

import pandas as pd
import plotly.express as px

def clean_text(stop_words='Yes'):
    data = load_data()
    data = tokenize(data)

    if stop_words == 'Yes':
        data = remove_stop_words(data)

    data = semantic_meaning(data)

    return data

def game_graph(results: pd.DataFrame,func,game: str):

        data = results[results['game'] == game]
        results_game = func(data)

        left_col,right_col = st.columns(2)
        with left_col:
            st.pyplot(results_game['fig1'])
        with right_col:
            st.pyplot(results_game['fig2'])


def main():
    data = clean_text()
    #data = extract_game_features(data)

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
        game_graph(data,word_cloud,game=game)


    st.divider()

    hist_tokens(data)

    #BY GAME    

    for game in games:
        data_g = data[data['game'] == game]
        hist_tokens(data_g)


    lengths = reviews_length(data)

    col_len1,col_len2 = st.columns(2)

    col_len1.metric('Word Mean Length ',lengths['word_length'].mean())
    col_len2.metric('Sentence Mean Length ',lengths['sentence_length'].mean())

    box1 = px.box(lengths,x='game',y='word_length')
    st.plotly_chart(box1)

    col_lens1,col_lens2 = st.columns(2)
    
    with col_lens1:
        st.plotly_chart(px.histogram(lengths['word_length']))
    with col_lens2:
        st.plotly_chart(px.histogram(lengths['content_length']))
    

    data2 = semantic_meaning(clean_text(stop_words='Not'))
    df = features_weighted = Word_Vector(data2,method='tfidf').sort_values(ascending=False).head(10)

    fig1 = px.bar(df,y=df.index,x=df.values)

    st.plotly_chart(fig1)

if __name__ == '__main__':
    main()
