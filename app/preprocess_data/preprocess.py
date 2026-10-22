import nltk
import pandas as pd
import string
import numpy as np
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer,PorterStemmer

import spacy

from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
from spellchecker import SpellChecker

def tokenize(data: pd.DataFrame) -> pd.DataFrame:

    nltk.download('punkt')
    nltk.download('punkt_tab')
    data.dropna(inplace=True)
    data['content'] = data['content'].astype(str).str.lower()
    data['word_token'] = data['content'].apply(nltk.word_tokenize)
    data['sentence_token'] = data['content'].apply(nltk.sent_tokenize)

    return data

    
def remove_stop_words(data):

    nltk.download('stopwords')
    gacha_stopwords = ['game','games','history','story','characters','character','banner','gacha','events','update',
                             'gaming','play','player','players','mobile','phone','summon','summons','summoning',
                             'pull','pulls','pulling','roll','rolls','rolling','banners','spark','pity',
                             'rate','rates','drop','drops','graphic','meta','s','ss','star','stars','stats',
                             'stat','list','tier','level','lvl']
     
    
    stopwords_set = set(stopwords.words('english') + gacha_stopwords)
    punctuation_set = set(string.punctuation)

    data['word_token'] = [
        [word for word in row if word not in stopwords_set and word not in punctuation_set]
        for row in data['word_token']
    ]

    return data

     
def correct_text(data):

    spellchecker = SpellChecker()
    text = data['content'].to_list()

    data['content'] = [[spellchecker.correction(w) for w in review] 
                        for review in text]

    return data


def semantic_meaning(data: pd.DataFrame,method: str ='lemmatize') -> pd.DataFrame:

    if method == 'lemmatize':
        nltk.download('wordnet')
        lemmatizer = WordNetLemmatizer()

        data['word_token'] = [
                        [lemmatizer.lemmatize(word) for word in row]
                        for row in data['word_token']
                        ]

    elif method == 'stemming':
            stemmer = PorterStemmer()

            data['word_token'] = [
                [stemmer.stem(word) for word in row]
                for row in data['word_token']
            ]
            
        #error: not method name

    return data


#counts
def Word_Vector(data: pd.DataFrame,max_features: int =1000,
                min_df: int = 40,max_df: int = 3000,method: str ='bow')  -> pd.DataFrame:

    df = data['content'].to_list()

    if method == 'bow':
        bow = CountVectorizer(ngram_range=(1,3),max_features=max_features,min_df=min_df,max_df=max_df)
        X = bow.fit_transform(df)

        summ = np.asarray(X.sum(axis=0)).ravel()
        vocab = bow.get_feature_names_out()
        bow_df = pd.Series(summ,index=vocab)

        return bow_df

    elif method == 'tfidf':
        tfidf = TfidfVectorizer(ngram_range=(1,3),max_features=max_features,min_df=min_df)
        X = tfidf.fit_transform(df)

        summ = np.asarray(X.sum(axis=0)).ravel()
        vocab = tfidf.get_feature_names_out()
        tidif_df = pd.Series(summ,index=vocab)

        return tidif_df
    
        #error: not method name
