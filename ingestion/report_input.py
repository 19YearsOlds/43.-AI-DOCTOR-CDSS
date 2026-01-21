from ingestion.normalization import normalize_text

def load_report(path):
    with open(path, "r") as f:
        return normalize_text(f.read())