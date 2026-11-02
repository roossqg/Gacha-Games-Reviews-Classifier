import nltk
import pandas as pd
import string
import numpy as np
from nltk.corpus import stopwords

import spacy
from spacy.tokens import Doc

from Evaluations.time_func import timer
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
from spellchecker import SpellChecker

#flow: 1: clean -> tokens -> remove stop -> correct
#2: stopwords -> word_vector-cloud

@timer
def tokenize(data: pd.DataFrame,lemma: bool =True,caps: bool=True) -> pd.DataFrame:

    nlp = spacy.load('en_core_web_sm',disable=['parse','ner'])
    nlp.add_pipe('sentencizer')
    
    data = data.dropna(subset=['content']).copy()

    if caps:
        docs = list(nlp.pipe(data['content'].astype(str).str.lower().tolist()))
    else:
        docs = list(nlp.pipe(data['content'].astype(str).tolist()))
        

    if lemma:
        data['word_token'] = [[token.lemma_ for token in doc] for doc in docs]

    else:
        data['word_token'] = [[token.text for token in doc] for doc in docs]

    data['sentence_token'] = [[sent.text for sent in doc.sents] for doc in docs]

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

@timer
def correct_text(data):

    spellchecker = SpellChecker(distance=1)
    nlp = spacy.load('en_core_web_sm')

    vocab = {w for review in data['word_token'] for w in review}
    unknown = spellchecker.unknown([w for w in vocab if w.isalpha()])

    mappping = {w: (spellchecker.correction(w) or w) for w in unknown}

    data['word_token'] = [[mappping.get(w,w) for w in review]
                    for review in data['word_token']]

    data['content'] = [Doc(nlp.vocab,words=re_tokens).text for re_tokens in data['word_token']]

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
