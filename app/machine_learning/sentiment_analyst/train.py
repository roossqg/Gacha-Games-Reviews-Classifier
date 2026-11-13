from preprocess_data.preprocess import Word_Vector, correct_text,tokenize
from preprocess_data.load import load_data

import pandas as pd
import numpy as np
from machine_learning.sentiment_analyst.model import SoftmaxRegressor
#clean -> label llm -> data val -> train-pipeline -> validation-analyst

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
#- batch predict-processing-train

def load_data_for_modeling():
    data = pd.read_csv('Gacha_Reviews/vader_sentiment_dataset.csv')

    X = Word_Vector(data,method='tfidf')
    y = data[['positive_score','negative_scores','neutral_scores']]

    x_train,x_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=33)

    return x_train,x_test,y_train,y_test
    

def imports_data_for_classify(caps=True,lemma=True):

    data = load_data()
    data_preprocessed = tokenize(data,caps=caps,lemma=lemma)
    data_clean = correct_text(data_preprocessed)

    X = Word_Vector(data_clean,method='tfidf')

    return X


def eval_multi_proba(y_pred,y_true):
    cols = ['positive_scores','negative_scores','neutral_scores']
    scores_mae = {}

    for i,col_name in enumerate(cols):

        mae = mean_absolute_error(
            y_true[:,i],
            y_pred[:,i]

        )
        scores_mae[col_name] = mae

    epilson = 1e-12

    cross_entropy_err = - np.mean(
        np.sum(
        y_true * np.log(np.clip(y_pred,epilson,1))
        ),axis=1
    )

    return cross_entropy_err,scores_mae



def train_and_scores():

    x_train,x_test,y_train,y_test = load_data_for_modeling()

    features = imports_data_for_classify()

    model = SoftmaxRegressor()
    model.fit(x_train,y_train)

    test_pred = model.predict_proba(x_test)
    #train_pred = model.predict_proba(x_train)

    test = eval_multi_proba(test_pred,y_test)

    labels = model.predict_proba(features)

    dataset = pd.concat([features,labels],axis=1)
    dataset.to_csv('sentiment_dataset.csv')

    return f'Eval at Test set: Cross-Entropy{test[0]},MAE of Prob dist: {test[1]}'
   

train_and_scores()







    











