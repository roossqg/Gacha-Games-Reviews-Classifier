from wordcloud import WordCloud
#from huggingface_hub import pipeline 

import plotly.express as px
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

from preprocess_data.load import load_data
from preprocess_data.preprocess import clean_text_data,semantic_meaning,Word_Vector

def hist_tokens(data: pd.DataFrame) -> dict:

    df = data['word_token'].value_counts()
    df2 = data['sentene_token'].value_counts()

    fig = px.histogram(df)
    fig2 = px.histogram(df2)

    return {'fig': fig ,'fig2': fig2}

    #data tokens -> sum vectors features


def reviews_length(data: pd.DataFrame) -> dict:

    data['word_length'] = data['word_token'].len()
    data['sentene_length'] = data['sentence_token'].len()

    data['review_length'] = data['review'].len()

    return data


def word_cloud(data: pd.DataFrame) -> dict:

    full_text = " ".join(review for review in data['word_token'].dropna().astype(str))

    wc_with_stopwords = WordCloud(background_color='white',stopwords=ENGLISH_STOP_WORDS).generate(
        full_text)
    wc_without_stopwords = WordCloud(background_color='white').generate(full_text)

    fig1,ax1 = plt.subplots()
    ax1.imshow(wc_with_stopwords,interpolation='bilinear')

    fig2,ax2 = plt.subplots()
    ax2.imshow(wc_without_stopwords,interpolation='bilinear')

    return {'fig1': fig1,'fig2': fig2}





    

