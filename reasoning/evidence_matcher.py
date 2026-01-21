from knowledge.guidelines import GUIDELINES

def match(diseases):
    return {d: GUIDELINES.get(d, "") for d in diseases}