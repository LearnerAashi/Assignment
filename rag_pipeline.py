from langchain.llms import HuggingFaceHub
from langchain.chains import RetrievalQA

def setup_qa_chain(vectordb):
    """
    Set up a QA chain using Hugging Face model.

    Args:
        vectordb (FAISS): FAISS vector database.

    Returns:
        RetrievalQA: QA Chain.
    """
    llm = HuggingFaceHub(
        repo_id="google/flan-t5-small",
        model_kwargs={"temperature":0.5, "max_length":512}
    )
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectordb.as_retriever()
    )
    return qa_chain
# ---------------------------------------
# from langchain.chains import RetrievalQA
# from langchain import PromptTemplate
# template = """
# Use the following pieces of context to provide the exact answer as written in the document. 
# If the answer is not explicitly stated, provide the most relevant and probable answer based on the context.


# {context}

# Question: {question}

# """

# PROMPT = PromptTemplate(
#     template=template, input_variables=["context", "question"]
# )

# chain_type_kwargs = {"prompt": PROMPT}
# qa1 = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=new_db.as_retriever(), chain_type_kwargs=chain_type_kwargs)

# query = """
# what is the book ?
# """
# output = qa1.run(query)
# output

# # "KB18798464 - How to switch DNS for the OneView platform in the Cloud Acceleration Project"