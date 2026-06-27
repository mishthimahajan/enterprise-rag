import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def retrieve(query,
             chunks,
             embeddings,
             top_k=5):

    query_embedding = model.encode([query])[0]

    similarities = []

    for idx, emb in enumerate(embeddings):

        score = np.dot(
            query_embedding,
            emb
        )

        similarities.append(
            (score, chunks[idx])
        )

    similarities.sort(
        reverse=True
    )

    return similarities[:top_k]