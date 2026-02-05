import numpy as np

class EndeeVectorStore:
    def __init__(self):
        self.vectors = []
        self.texts = []

    def insert(self, vector, text):
        self.vectors.append(vector)
        self.texts.append(text)

    def cosine_similarity(self, a, b):
        return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

    def search(self, query_vector, top_k=2):
        scores = []
        for vec, txt in zip(self.vectors, self.texts):
            score = self.cosine_similarity(query_vector, vec)
            scores.append((score, txt))
        scores.sort(reverse=True, key=lambda x: x[0])
        return scores[:top_k]
