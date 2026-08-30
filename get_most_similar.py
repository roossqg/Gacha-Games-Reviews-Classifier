import chromadb
from Gacha_Reviews.Ai_Models.embedding_model import emb_model

client = chromadb.PersistentClient(path='./chromadb')
collection = client.get_collection(name='gachas_review')

def get_similar_reviews(text_input,n_similars):
    emb_text = emb_model.encode([text_input])

    query_vectors = collection.query(
        query_embeddings = emb_text,
        n_results = n_similars,
        include = ["embeddings", "documents", "distances"]
    )

    return query_vectors


def get_vector_database(path='./chromadb',name='gachas_review'):
    client = chromadb.PersistentClient(path=path)

    collection = client.get_collection(name=name)

    print(f'Collection: {collection.peek()}\n Vector Count: {collection.count()}')


#print(get_similar_reviews('I love genhsin waifus',2))
print(get_vector_database())