import pandas as pd
from Gacha_Reviews.app.sentiment_and_topic.train import eval_multi_proba
import numpy as np

def eval():
    data = pd.read_csv('Gacha_Reviews/app/sentiment_and_topic/datasets_by_llm/sentiment_dataset.csv')[:4000]
    y_pred = data[['positive_score','negative_scores','neutral_scores']]

    d = pd.read_csv('Gacha_Reviews/app/sentiment_and_topic/datasets_by_llm/vader_sentiment_dataset.csv')
    y_true = d[['positive_score','negative_scores','neutral_scores']]

    data_entropy = np.mean(-np.sum(y_true * np.log(y_true + 1e-15),axis=1))

    cross_entropy,mae = eval_multi_proba(y_pred,y_true)

    metrics = {
        'Probability_Class_Entropy': cross_entropy,
        'MAE of Probabilities': mae, 
        'KL Divergence': cross_entropy - data_entropy
    }

    return metrics


if __name__ == '__main__':
    print(eval())