# !pip install numpy==1.26.4
# !python -m spacy download en_core_web_sm
import spacy
from keybert import KeyBERT

def load_models():
    nlp = spacy.load("en_core_web_sm")
    kw_model = KeyBERT(model="sentence-transformers/all-MiniLM-L6-v2")
    return nlp, kw_model

def generate_ontology(text: str) -> dict:
    """
    Generate an ontology containing characters, locations, and themes.

    Args:
        text (str): Book text.

    Returns:
        dict: Ontology structure.
    """
    nlp, kw_model = load_models()
    doc = nlp(text)

    characters = list(set([ent.text for ent in doc.ents if ent.label_ == "PERSON"]))
    locations = list(set([ent.text for ent in doc.ents if ent.label_ in ("GPE", "LOC")]))
    keywords = kw_model.extract_keywords(text, top_n=10, stop_words='english')
    themes = [kw[0] for kw in keywords]

    ontology = {
        "characters": sorted(set(characters))[:15],
        "locations": sorted(set(locations))[:10],
        "themes": themes
    }
    return ontology

# ------------------------------------------------------------------------------------------------------------

# import spacy

# # Load the spaCy model
# nlp = spacy.load("en_core_web_sm")

# # Process the text to extract entities
# doc = nlp(text)

# # Extract entities and relationships
# entities = {ent.text: ent.label_ for ent in doc.ents}
# print("Extracted Entities:", entities)

# from langchain.chat_models import AzureChatOpenAI
# import openai
# model= "mmc-tech-gpt-4o-mini-128k-2024-07-18"
# def generate_ontology(text):
#     prompt = f"""
#     Extract an ontology from the following text. 
#     Identify:
#     - Characters
#     - Locations
#     - Important Events
#     - Relationships between characters

#     Return output in JSON format.

#     Text: {text[:3000]}  # Limit to first 3000 chars for speed
#     """

#     response = openai.ChatCompletion.create(
#         model= "mmc-tech-gpt-4o-mini-128k-2024-07-18",
#         engine=model,
        
#         messages=[{"role": "user", "content": prompt}]
#     )

#     ontology = response['choices'][0]['message']['content']
#     return ontology

