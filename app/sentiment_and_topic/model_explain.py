from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import *

from Gacha_Reviews.app.data_handle.preprocess_data.preprocess import Word_Vector, correct_text,tokenize
from Gacha_Reviews.app.data_handle.preprocess_data.load import load_data
from Gacha_Reviews.app.data_handle.preprocess_data import *
from Gacha_Reviews.app.data_handle.preprocess_data.preprocess import *
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

import shap
import lime

def train_data(caps=True,lemma=True):
    
    model = SentimentIntensityAnalyzer()

    data = pd.read_csv('Gacha_Reviews/app/sentiment_and_topic//vader_sentiment_dataset.csv')
    data_limited = data['content'].tolist()[:5000]

    for review in data_limited:
        scores = model.polarity_scores(review)




def model_explainability():
    







#



