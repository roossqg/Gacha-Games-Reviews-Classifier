import streamlit as st
from app.preprocess_data.load import load_data
from app.preprocess_data.preprocess import clean_text_data,semantic_meaning,Word_Vector
from app.analyst import word_cloud,hist_tokens

import plotly.express as px

def words_meaning():
    data = load_data()
    data = clean_text_data(data)
    data = semantic_meaning(data)
    data2 = Word_Vector(data)

    return data

def main():
    data = words_meaning()

    col1,col2 = st.columns(2)

    results_word_cloud = word_cloud(data)

    with col1:
        st.pyplot(results_word_cloud['fig'])

    with col2:
        st.pyplot(results_word_cloud['fig2'])

    results_count_tokens = hist_tokens(data)

    st.divider()

    col4,col5 = st.columns(2)

    with col4:
        st.pyplot(results_count_tokens['fig'])

    with col5:
        st.pyplot(results_count_tokens['fig2'])    


    df = features_weighted = Word_Vector(method='tfidf')
    st.dataframe(df.head(5))

    df_count = df.sum(axis=0)

    fig1 = px.histogram(df_count)

    st.plotly_chart(fig1)

    
