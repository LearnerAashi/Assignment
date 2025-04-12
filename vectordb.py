from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS

def chunk_text(text: str):
    """
    Split text into smaller chunks.

    Args:
        text (str): Raw text.

    Returns:
        List[str]: List of text chunks.
    """
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    return splitter.split_text(text)

def create_vector_db(chunks):
    """
    Create a FAISS vector store from text chunks.

    Args:
        chunks (List[str]): List of text chunks.

    Returns:
        FAISS: FAISS vector database object.
    """
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectordb = FAISS.from_texts(chunks, embedding=embeddings)
    return vectordb
