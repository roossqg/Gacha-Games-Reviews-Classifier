import streamlit as st
from app.sentiment_and_topic.graphs_sentiments import counts,histogram,bar,boxplot,classify_sentiment_by_scores

import pandas as pd

def main():

    pre_data = pd.read_csv('Gacha_Reviews/app/sentiment_and_topic/datasets_by_llm/vader_sentiment_dataset.csv')
    data = classify_sentiment_by_scores(pre_data)

    result1 = counts(data)
    st.plotly_chart(result1)

    result2 = histogram(data)
    col1,col2,col3 = st.columns(3)
    with col1:
        st.plotly_chart(result2['fig1'])
    with col2:
        st.plotly_chart(result2['fig2'])
    with col3:
        st.plotly_chart(result2['fig3'])

    #result3
    bar(data)

    result3 = boxplot(data)
    col4,col5,col6 = st.columns(3)
    with col4:
        st.plotly_chart(result3['fig1'])
    with col5:
        st.plotly_chart(result3['fig2'])
    with col6:
        st.plotly_chart(result3['fig3'])
    

if __name__ == "__main__":
    main()
