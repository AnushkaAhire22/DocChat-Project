import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def create_or_load_vector_store(text_chunks):
    embeddings = model.encode(text_chunks)
    index = faiss.IndexFlatL2(len(embeddings[0]))
    index.add(np.array(embeddings))
    return {"index": index, "texts": text_chunks}

def search_docs(store, query, top_k=3):
    query_vec = model.encode([query])
    D, I = store["index"].search(np.array(query_vec), top_k)
    return [store["texts"][i] for i in I[0]]

# # updated for highlight
# def search_docs(store, query, top_k=3):
#     query_vec = model.encode([query])
#     D, I = store["index"].search(np.array(query_vec), top_k)
#     return [store["texts"][i] for i in I[0]], I[0]
