import streamlit as st

from app.data_handle.analyst import word_cloud, hist_tokens, reviews_length
from app.data_handle.preprocess_data.load import load_data
from app.data_handle.preprocess_data.preprocess import (
    Word_Vector,
    correct_text,
    remove_stop_words,
    tokenize,
)

import pandas as pd
import plotly.express as px


@st.cache_data()
def clean_text(stop_words='Yes',lemma=True):
    data = load_data()
    data = tokenize(data,lemma=lemma)
    data = correct_text(data)

    if stop_words == 'Yes':
        data = remove_stop_words(data)

    return data

def game_graph(results: pd.DataFrame,func,game: str):

        data = results[results['game'] == game]
        results_game = func(data)

        st.markdown(f"### 🎮 {game}")
        left_col,right_col = st.columns(2)
        with left_col:
            st.pyplot(results_game['fig1'])
        with right_col:
            st.pyplot(results_game['fig2'])


def main():
   
    data = clean_text()
    #data = extract_game_features(data)

    metric_reviews, metric_games = st.columns(2)
    metric_reviews.metric("Reviews loaded", f"{len(data):,}")
    metric_games.metric("Games in dataset", data["game"].nunique())

    st.divider()
    st.header("☁️ Featured Vocabulary")

    #TOTAL
    results_word_cloud = word_cloud(data)

    col1,col2 = st.columns(2)
    with col1:
        st.caption("Terms without stop words")
        st.pyplot(results_word_cloud['fig1'])

    with col2:
        st.caption("Terms including stop words")
        st.pyplot(results_word_cloud['fig2'])

    games =  ['Genshin Impact','Honkai Star Rail','Zenless Zone Zero',
            'Wuthering Waves','Blue Archive']

    #BY GAME 
    st.header("🎮 Word Clouds by Game")

    for game in games:
        game_graph(data,word_cloud,game=game)

    st.divider()

    st.header("🔤 Term and Phrase Frequency")
    hist_tokens(data)

    #BY GAME    

    for game in games:
        data_g = data[data['game'] == game]
        st.subheader(f"🎮 {game}")
        hist_tokens(data_g)


    lengths = reviews_length(data)

    st.header("📏 Review Length")
    col_len1,col_len2 = st.columns(2)

    col_len1.metric('Average Words per Review',lengths['word_length'].mean())
    col_len2.metric('Average Sentences per Review',lengths['sentence_length'].mean())

    box1 = px.box(lengths,x='game',y='word_length')
    st.plotly_chart(box1)

    col_lens1,col_lens2 = st.columns(2)
    
    with col_lens1:
        st.plotly_chart(px.histogram(lengths['word_length']))
    with col_lens2:
        st.plotly_chart(px.histogram(lengths['content_length']))
    

    data2 = clean_text(stop_words='Not',lemma=False)
    df = Word_Vector(data2,method='tfidf').sort_values(ascending=False).head(10)

    st.header("✨ Top TF-IDF Terms")
    fig1 = px.bar(df,y=df.index,x=df.values)

    st.plotly_chart(fig1)

if __name__ == '__main__':
    main()
