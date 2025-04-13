# Assignment

# Ontology based RAG Search App

## Project Flow

Text (Book) -> Ontology Extraction -> Vector Database (FAISS) -> Answer Questions (RAG) -> Streamlit APP

---

## Tech Stack
- **Backend**: Python
- **Frontend**: Streamlit
- **Embedding Model**: Sentence Transformers / Openai Embedding
- **Vector DB**: FAISS/ Graph based - Neo4j
- **NER + Keywords**: Spacy + KeyBERT / Prompt Engineering 
- **RAG Model**: Huggingface Flan-T5/ Openai

---

## Instructions

git clone 
cd 
pip install -r requirements.txt
streamlit run app.py

## Components
Download_book Extract text from any book reference book given
Ontology Extract entities, relationships, concepts automatically	spacy, LLM, networkx	Prompt LLM to generate ontology from text chunks
Chunker	Split book into meaningful parts (chapters, paragraphs)	langchain.text_splitter, nltk	Choose chunking based on semantic units
Embedder	Create vector embeddings	sentence-transformers, OpenAI Embeddings, HuggingFace	
Vector Database	Store embeddings for retrieval	FAISS, Chroma, Pinecone	Start with FAISS (local)
Retriever	Search similar chunks based on user query	langchain retriever	Ontology can assist in refining search
Generator	Generate answer using chunks + query	OpenAI GPT-4, HuggingFace LLMs	Standard RAG
Streamlit UI	Input book, input query, show ontology, show answer	streamlit	Swap any book easily
