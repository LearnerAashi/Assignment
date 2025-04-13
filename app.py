import streamlit as st

from download_book import download_book
from ontology import generate_ontology
from vectordb import chunk_text,create_vector_db
from rag_pipeline import setup_qa_chain


# ----------- Settings -----------
DEFAULT_BOOK_URL = "https://www.gutenberg.org/cache/epub/1342/pg1342.txt"

# ----------- Streamlit App -----------
st.set_page_config(page_title="Ontology Based RAG App", layout="wide")
st.title("📚 Ontology-Based RAG Search App")

# Load Book
if "raw_text" not in st.session_state:
    with st.spinner("Downloading book..."):
        raw_text = download_book(DEFAULT_BOOK_URL)
        st.session_state["raw_text"] = raw_text
else:
    raw_text = st.session_state["raw_text"]

# Generate Ontology
if "ontology" not in st.session_state:
    with st.spinner("Generating Ontology..."):
        ontology = generate_ontology(raw_text)
        st.session_state["ontology"] = ontology
else:
    ontology = st.session_state["ontology"]

st.subheader("📖 Ontology from the Book")
st.json(ontology)

# Create Vector Store
if "vectordb" not in st.session_state:
    with st.spinner("Preparing vector database..."):
        chunks = chunk_text(raw_text)
        vectordb = create_vector_db(chunks)
        st.session_state["vectordb"] = vectordb
else:
    vectordb = st.session_state["vectordb"]

# User Query
st.subheader("🔍 Ask a Question")
query = st.text_input("Type your question here:")

if query:
    with st.spinner("Searching for the answer..."):
        qa_chain = setup_qa_chain(vectordb)
        answer = qa_chain.run(query)
        st.success(answer)

# Upload Your Own Book
st.sidebar.header("📥 Upload a New Book")
uploaded_file = st.sidebar.file_uploader("Upload a .txt file", type=["txt"])

if uploaded_file:
    with st.spinner("Loading uploaded book..."):
        raw_text = uploaded_file.read().decode("utf-8")
        st.session_state["raw_text"] = raw_text
        st.session_state["ontology"] = generate_ontology(raw_text)
        chunks = chunk_text(raw_text)
        st.session_state["vectordb"] = create_vector_db(chunks)
    st.sidebar.success("Uploaded new book! Now ask away.")


# app.py
import streamlit as st
from utils import download_book, load_text
from ontology import generate_ontology
from embedder import chunk_text, embed_chunks, build_faiss_index
from rag_pipeline import retrieve_chunks, answer_query

# --------------- Configuration ---------------
BOOK_URL = "https://www.gutenberg.org/cache/epub/1342/pg1342.txt"
BOOK_PATH = "data/book.txt"

# --------------- App Start ---------------
st.title("📖 Ontology-based RAG Search")

# Step 1: Load Book
if st.button("Download Book"):
    download_book(BOOK_URL)
    st.success("Book downloaded successfully!")

# Step 2: Load text
text = load_text(BOOK_PATH)
st.text_area("Book Preview", text[:5000], height=200)

# Step 3: Create Ontology
if st.button("Generate Ontology"):
    ontology = generate_ontology(text)
    st.write("Ontology Concepts:")
    st.write(ontology)

# Step 4: Chunk & Embed
chunks = chunk_text(text)
model, embeddings = embed_chunks(chunks)
index = build_faiss_index(embeddings)

# Step 5: Accept Query
query = st.text_input("Ask your question about the book:")

if st.button("Get Answer"):
    if query:
        retrieved = retrieve_chunks(query, model, index, chunks)
        answer = answer_query(retrieved, query)
        st.success(f"Answer: {answer}")
    else:
        st.warning("Please enter a query.")

