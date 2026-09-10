import nltk
import pandas as pd
import string

from nltk.corpus import stopwords
from load import load_data

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

def clean_text_data():
    data = load_data()

    #data['content'] = (nltk.sent_tokenize(data['content'].to_list())).toarray()
    data['content'] = data['content'].str.lower()

    for i in data.index:
        data.loc[i,'content'] = nltk.sent_tokenize(data[i,'content'])
        data.loc[i,'content'] = [char for char in data[i,'content'].to_list() 
            if char not in string.punctuation and char not in stopwords.words]

    #lamtize

    return data





