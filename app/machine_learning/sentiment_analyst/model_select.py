from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV

from sklearn.metrics import *

from preprocess_data import *
from preprocess_data.preprocess import *

pipe = Pipeline([])


log_reg = LogisticRegression()
svc = SVC()
nb = MultinomialNB()


grid = GridSearchCV()



