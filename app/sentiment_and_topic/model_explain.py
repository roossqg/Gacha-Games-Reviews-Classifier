from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import *

from Gacha_Reviews.app.data_handle.preprocess_data.preprocess import Word_Vector, correct_text,tokenize
from Gacha_Reviews.app.data_handle.preprocess_data.load import load_data
from model import SoftmaxRegressor
from Gacha_Reviews.app.data_handle.preprocess_data import *
from Gacha_Reviews.app.data_handle.preprocess_data.preprocess import *


import shap

def train_data(caps=True,lemma=True):
#pipe = Pipeline([
    model = Pipeline([
        TfidfVectorizer(TfidfVectorizer(ngram_range=(1,3),max_features=4000)),
        SoftmaxRegressor()
    ])

    data = pd.read_csv('Gacha_Reviews/app/sentiment_and_topic//vader_sentiment_dataset.csv')

    model.fit_predict(data)


def model_explainability():
    







#



