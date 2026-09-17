from wordcloud import WordCloud
from huggingface_hub import pipeline 

import plotly.express as px
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

from app.preprocess_data.load import load_data
from app.preprocess_data.preprocess import clean_text_data,semantic_meaning,Word_Vector

def hist_tokens(data: pd.DataFrame) -> dict:

    df = data['word_token'].value_counts()
    df2 = data['sentene_token'].value_counts()

    fig = px.histogram(df)
    fig2 = px.histogram(df2)

    return {'fig': fig ,'fig2': fig2}

    #data tokens -> sum vectors features


def word_cloud(data: pd.DataFrame) -> dict:

    wc_with_stopwords = WordCloud(data['word_token'],background_color='white',stopwords=ENGLISH_STOP_WORDS).generate()
    wc_without_stopwords = WordCloud(data['word_token'],background_color='white').generate()

    fig1,ax1 = plt.subplots()
    ax1.imshow(wc_with_stopwords,interpolation='bilinear')

    fig2,ax2 = plt.subplots()
    ax2.imshow(wc_without_stopwords,interpolation='bilinear')

    return {'fig1': fig1,'fig2': fig2}





    

