import pandas as pd
from Gacha_Reviews.app.sentiment_and_topic.train import eval_multi_proba

data = pd.read_csv('Gacha_Reviews/app/sentiment_and_topic/sentiment_dataset.csv')[:4000]
print(data)
y_pred = data[['positive_score','negative_scores','neutral_scores']]

d = pd.read_csv('Gacha_Reviews/app/sentiment_and_topic/vader_sentiment_dataset.csv')
y_true = d[['positive_score','negative_scores','neutral_scores']]

r,w = eval_multi_proba(y_pred,y_true)
print(r,w)