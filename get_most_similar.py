import chromadb
from Gacha_Reviews.embedding_model import emb_model

client = chromadb.PersistentClient(path='./chromadb')
collection = client.get_collection(name='gachas_review')

def query_similar_reviews(text_input,n_similars):
    emb_text = emb_model.encode([text_input])

    query_vectors = collection.query(
        query_embeddings = emb_text,
        n_results = n_similars,
        include = ["embeddings", "documents", "distances"]
    )

    return query_vectors['documents']


print(query_similar_reviews('I love genhsin waifus',2))