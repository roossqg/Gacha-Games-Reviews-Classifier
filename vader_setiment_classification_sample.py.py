from ollama import chat
import pandas as pd
from app.preprocess_data.load import load_data
from app.preprocess_data.preprocess import correct_text,tokenize
import random

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

#solutions:
#1.vader + terms
#2.vader -> tf-idf-ml



def get_data_for_label(caps=True,lemma=True):
    data = load_data()
    data_preprocessed = tokenize(data,caps=caps,lemma=lemma)
    data_clean = correct_text(data_preprocessed)

    return data_clean


#data -> model + instruct + output-stucture  + classify


def labels(k:int = 4000):

    data_reviews_list = get_data_for_label(caps=False,lemma=False)['content'].tolist()
    sample = random.sample(data_reviews_list,k=k)
    model = SentimentIntensityAnalyzer()

    #gacha_lexicon = {}
    #model.lexicon.update(gacha_lexicon)

    neg_scores = []
    neu_scores = []
    pos_scores = []
    sentiment_labels = []

    for review in sample:

        sentiment_dict = model.polarity_scores(review)
        neg_scores.append(sentiment_dict['neg'])
        neu_scores.append(sentiment_dict['neu'])
        pos_scores.append(sentiment_dict['pos'])

        if sentiment_dict['compound'] >= 0.05:
            sentiment_labels.append(2)
        elif sentiment_dict['compound'] <= -0.05:
            sentiment_labels.append(0)
        else:
            sentiment_labels.append(1)

    dataset = pd.DataFrame({
        'content':sample,
        'sentiment': sentiment_labels,
        'positive_score': pos_scores,
        'negative_scores': neg_scores,
        'neutral_scores': neu_scores
    })

    dataset.to_csv('vader_sentiment_dataset.csv')

    










