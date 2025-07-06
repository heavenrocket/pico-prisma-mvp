import spacy

nlp = spacy.load("en_core_sci_sm")

def extract_pico(abstract):
    doc = nlp(abstract)
    entities = [ent.text for ent in doc.ents]
    return {
        "P": entities[0] if len(entities) > 0 else "",
        "I": entities[1] if len(entities) > 1 else "",
        "C": entities[2] if len(entities) > 2 else "",
        "O": entities[3] if len(entities) > 3 else "",
    }
