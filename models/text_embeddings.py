from sklearn.feature_extraction.text import TfidVectorizer

class TextEmbedder:
    def embed(self, texts):
        v = TfidVectorizer()
        return v.fit_transform(texts).toarray()