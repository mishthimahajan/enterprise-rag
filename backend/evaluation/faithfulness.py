import numpy as np
from services.embedder import create_embeddings


def cosine_similarity(a, b):
    a = np.array(a)
    b = np.array(b)

    return np.dot(a, b) / (
        np.linalg.norm(a) * np.linalg.norm(b)
    )


def calculate_faithfulness(answer, context):

    if not answer or not context:
        return 0.0

    answer_embedding = create_embeddings(answer)[0]

    context_embedding = create_embeddings(context)[0]

    score = cosine_similarity(
        answer_embedding,
        context_embedding
    )

    return round(
        float(score),
        4
    )