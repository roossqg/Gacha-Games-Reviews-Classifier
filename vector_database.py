import chromadb
import pandas as pd
from Gacha_Reviews.Ai_Models.embedding_model import emb_model

import time

start_time = time.perf_counter()

client = chromadb.PersistentClient(path='./chromadb')

collection = client.get_collection(name='gachas_review')

data = pd.read_csv('Datasets/wuwa_processed.csv')

docs = (data['content'].tolist())[1000:]
ids = [str(1000+i) for i in range(len(docs))]
embeddings = [emb_model.encode(doc) for doc in docs]

end_time = time.perf_counter()
elapsed_time = end_time - start_time

print(f'Ready : n_emb: {len(embeddings)} in time: {elapsed_time}')

collection.add(
    documents = docs,
    embeddings = embeddings,
    ids = ids
)
