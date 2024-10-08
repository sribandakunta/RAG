from transformers import pipeline

# Load the Hugging Face text generation pipeline
generator = pipeline('text-generation', model='gpt-2')

def retrieve(query, top_k=5):
    # Create embedding for the query
    query_embedding = embedder.encode([query], convert_to_tensor=False)
    
    # Search in the FAISS index
    distances, indices = index.search(np.array(query_embedding), top_k)
    
    # Retrieve relevant documents
    relevant_docs = [corpus[idx] for idx in indices[0]]
    return relevant_docs

def generate_response(query, top_k=5):
    # Retrieve relevant documents
    relevant_docs = retrieve(query, top_k)
    
    # Concatenate the retrieved documents to form context
    context = ' '.join(relevant_docs)
    
    # Generate a response using the language model
    generated_text = generator(query + context, max_length=300, num_return_sequences=1)
    
    return generated_text[0]['generated_text']
