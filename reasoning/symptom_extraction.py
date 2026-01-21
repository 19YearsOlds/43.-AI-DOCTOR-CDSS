from knowledge.medical_ontology import CONCEPTS

def extract_symptoms(text):
    return [s for s in CONCEPTS if s in text]