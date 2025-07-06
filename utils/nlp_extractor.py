import spacy
import subprocess

def load_model():
    try:
        return spacy.load("en_core_sci_sm")
    except:
        subprocess.run(["python", "-m", "pip", "install", "https://github.com/allenai/scispacy/releases/download/v0.5.3/en_core_sci_sm-0.5.3.tar.gz"])
        return spacy.load("en_core_sci_sm")

nlp = load_model()

def extract_pico(abstract):
    doc = nlp(abstract)
    entities = [ent.text for ent in doc.ents]
    return {
        "P": entities[0] if len(entities) > 0 else "",
        "I": entities[1] if len(entities) > 1 else "",
        "C": entities[2] if len(entities) > 2 else "",
        "O": entities[3] if len(entities) > 3 else "",
    }
