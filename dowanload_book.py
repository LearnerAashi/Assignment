import requests

def download_book(url: str) -> str:
    """
    Download the book from the given URL.

    Args:
        url (str): URL to the book.

    Returns:
        str: Raw text content of the book.
    """
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"Failed to download book. Status code: {response.status_code}")
# ------------------------------------------------------------------------------------------------------
# import requests
# from langchain.schema import Document
# from langchain.text_splitter import CharacterTextSplitter

# # Fetch the text from the URL
# url = "https://www.gutenberg.org/cache/epub/1342/pg1342.txt"
# response = requests.get(url)
# text = response.text

# # Create a Document object
# document = Document(page_content=text, metadata={"source": url})

# print(document)


