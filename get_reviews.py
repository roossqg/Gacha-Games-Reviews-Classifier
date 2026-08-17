import chromadb

client = chromadb.PersistentClient(path='./chromadb')

collection = client.get_collection(name='gachas_review')

print(collection.peek())
print(collection.count())