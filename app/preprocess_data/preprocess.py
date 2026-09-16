import nltk
import pandas as pd
import string

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer,PorterStemmer
from load import load_data

from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

data = load_data()

def clean_text_data() -> pd.DataFrame:
    data = load_data()

    data.dropna(inplace=True)
    data['content'] = data['content'].astype(str).str.lower()
    data['word_token'] = data['content'].apply(nltk.word_tokenize)
    data['sentence_token'] = data['content'].apply(nltk.sent_tokenize)

    stopwords_set = set(stopwords.words())
    punctuation_set = set(string.punctuation)

    data['word_token'] = [
        [word for word in row if word not in stopwords_set and word not in punctuation_set]
        for row in data['word_token']
    ]

    return data


def semantic_meaning(data: pd.DataFrame,method: str ='lemmatize') -> pd.DataFrame:

    if method == 'lemmatize':
        lemmatizer = WordNetLemmatizer()

        data['word_token'] = [
                        [lemmatizer.lemmatize(word) for word in row]
                        for row in data['word_token']
                        ]

    elif method == 'stemming':
            stemmer = PorterStemmer()

            data['word_token'] = [
                [stemmer.stem(word) for word in row]
                for row in data['word_token']
            ]
            
        #error: not method name

    return data


#counts
def Word_Vector(data: pd.DataFrame,max_features: int =1000,min_df: int = 40,method: str ='bow')  -> pd.DataFrame:

    df = data['content'].to_list()

    if method == 'bow':
        bow = CountVectorizer(ngram_range=(1,3),max_features=max_features)
        X = bow.fit_transform(df)

        bow_df = pd.DataFrame(X.toarray(),columns=bow.get_feature_names_out())

        return bow_df

    elif method == 'tfidf':
        tfidf = TfidfVectorizer(ngram_range=(1,3),max_features=max_features)
        X = tfidf.fit_transform(df)

        tidif_df = pd.DataFrame(X.toarray(),columns=bow.get_feature_names_out())

        return tidif_df

    
        #error: not method name



print(clean_text_data())
#print(data.iloc[2,'content'])