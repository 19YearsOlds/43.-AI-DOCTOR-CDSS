from knowledge.symptom_disease_map import MAP

def generate(symptoms):
    scores = {}
    for disease, sxs in MAP.items():
        scores[disease] = len(set(symptoms) & set(sxs)) / len(sxs)
    return scores