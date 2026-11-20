import pandas as pd

from Gacha_Reviews.app.data_handle.preprocess_data.load import load_data
from Gacha_Reviews.app.data_handle.preprocess_data.preprocess import correct_text,tokenize
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer



def get_data_for_label(caps=True,lemma=True):
    data = load_data()
    data_preprocessed = tokenize(data,caps=caps,lemma=lemma)
    data_clean = correct_text(data_preprocessed)

    return data_clean


def labels():

    data = get_data_for_label(caps=False,lemma=False)
    data_reviews = data['content'].tolist()
    model = SentimentIntensityAnalyzer()

    #gacha_lexicon = {}
    #model.lexicon.update(gacha_lexicon)

    neg_scores = []
    neu_scores = []
    pos_scores = []
    sentiment_labels = []

    for review in data_reviews:

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
        'content':data_reviews,
        'game': data['game'].tolist(),
        'word_token': data['word_token'].tolist(),
        'sentence_token': data['sentence_token'].tolist(),
        'sentiment': sentiment_labels,
        'positive_score': pos_scores,
        'negative_scores': neg_scores,
        'neutral_scores': neu_scores
    })

    dataset.to_csv('vader_sentiment_dataset.csv')

    
if __name__ == '__main__':
    labels()









