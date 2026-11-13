from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV

from sklearn.metrics import *

from preprocess_data import *
from preprocess_data.preprocess import *


#pipe = Pipeline([
process = TfidfVectorizer(TfidfVectorizer(ngram_range=(1,3),max_features=4000))


log_reg = LogisticRegression()
svc = SVC()
nb = MultinomialNB()

data = pd.read_csv("Gacha_Reviews\vader_sentiment_dataset.csv")
X = process.fit_transform(data['content'])


#



