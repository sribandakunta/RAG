from sentence_transformers import SentenceTransformer
import os
import faiss
import numpy as np

# Initialize the sentence transformer model for embeddings
embedder = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

# Load and preprocess documents
corpus = []
doc_ids = []

def load_documents(data_dir):
    global corpus, doc_ids
    for idx, filename in enumerate(os.listdir(data_dir)):
        with open(os.path.join(data_dir, filename), 'r') as file:
            corpus.append(file.read())
            doc_ids.append(filename)

# Directory containing your text documents
data_dir = 'path_to_your_documents'
load_documents(data_dir)

# Convert documents to embeddings
corpus_embeddings = embedder.encode(corpus, convert_to_tensor=False)

# Save embeddings to a FAISS index
embedding_dim = corpus_embeddings.shape[1]
index = faiss.IndexFlatL2(embedding_dim)  # L2 distance

# Convert corpus embeddings to numpy array
corpus_embeddings = np.array(corpus_embeddings)

# Add embeddings to the FAISS index
index.add(corpus_embeddings)

print(f"Indexed {index.ntotal} documents.")
