import chromadb
from Ai_Models.embedding_model import emb_model

client = chromadb.PersistentClient(path='./chromadb')
collection = client.get_collection(name='gachas_review')

def get_similar_reviews(text_input: str,n_similars: int = 10):
    emb_text = emb_model.encode([text_input])

    query_vectors = collection.query(
        query_embeddings = emb_text,
        n_results = n_similars,
        include = ["documents", "distances"]
    )

    results = []
    for id ,doc,dist in zip(query_vectors['ids'][0],query_vectors['documents'][0],query_vectors['distances'][0]):
        if dist <= 17:
            results.append({'id':id ,'document': doc})


    return len(results)


def get_vector_database(path='./chromadb',name='gachas_review'):
    client = chromadb.PersistentClient(path=path)

    collection = client.get_collection(name=name)

    print(f'Collection: {collection.peek()}\n Vector Count: {collection.count()}')


#print(get_similar_reviews('I love genhsin waifus',20))
#print(get_vector_database())