import numpy as np
from services.embedder import create_embeddings


def cosine_similarity(a, b):
    a = np.array(a)
    b = np.array(b)

    return np.dot(a, b) / (
        np.linalg.norm(a) * np.linalg.norm(b)
    )


def calculate_relevance(question, chunks):

    if not chunks:
        return 0.0

    question_embedding = create_embeddings(question)[0]

    chunk_embeddings = create_embeddings(chunks)

    scores = [
        cosine_similarity(question_embedding, emb)
        for emb in chunk_embeddings
    ]

    return round(
        float(np.mean(scores)),
        4
    )