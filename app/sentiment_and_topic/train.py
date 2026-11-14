from Gacha_Reviews.app.data_handle.preprocess_data.preprocess import Word_Vector, correct_text,tokenize
from Gacha_Reviews.app.data_handle.preprocess_data.load import load_data

import pandas as pd
import numpy as np
from Gacha_Reviews.app.sentiment_and_topic.model import SoftmaxRegressor
#clean -> label llm -> data val -> train-pipeline -> validation-analyst

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.feature_extraction.text import TfidfVectorizer
#- batch predict-processing-train


def load_data_for_modeling():
    data = pd.read_csv('Gacha_Reviews/app/sentiment_and_topic/vader_sentiment_dataset.csv')
    text = data['content'].fillna('').astype(str)
    y = data[['positive_score', 'negative_scores', 'neutral_scores']]

    text_train,text_test,y_train,y_test = train_test_split(
        text, y, test_size=0.2, random_state=33
    )

    tfidf = TfidfVectorizer(ngram_range=(1,3),max_features=4000)
    x_train = tfidf.fit_transform(text_train)
    x_test = tfidf.transform(text_test)

    return x_train,x_test,y_train,y_test,tfidf
    

def imports_data_for_classify(tfidf,caps=False,lemma=False):

    data = load_data()
    data_preprocessed = tokenize(data,caps=caps,lemma=lemma)
    data_clean = correct_text(data_preprocessed)


    data_p = data_clean['content'].fillna('').astype(str)
    
    X = tfidf.transform(data_p)

    return data_clean,X


def eval_multi_proba(y_pred,y_true):
    y_pred = np.asarray(y_pred)
    y_true = np.asarray(y_true)
    cols = ['positive_score','negative_scores','neutral_scores']
    scores_mae = {}

    for i,col_name in enumerate(cols):

        mae = mean_absolute_error(
            y_true[:,i],
            y_pred[:,i]

        )
        scores_mae[f'{col_name}_MAE'] = mae

    epsilon = 1e-12

    cross_entropy_err = - np.mean(
        np.sum(
            y_true * np.log(np.clip(y_pred,epsilon,1)),
            axis=1
        )
    )

    return cross_entropy_err,scores_mae


def train_and_scores():

    x_train,_,y_train,_,tfidf = load_data_for_modeling()

    classification_data,features = imports_data_for_classify(tfidf)

    model = SoftmaxRegressor()
    model.fit(x_train,y_train.to_numpy(dtype=float))

    labels = model.predict_proba(features)

    score_columns = ['positive_score','negative_scores','neutral_scores']
    classification_data[score_columns] = labels
    classification_data.to_csv('sentiment_dataset.csv')

    return labels
   

if __name__ == '__main__':
    train_and_scores()





