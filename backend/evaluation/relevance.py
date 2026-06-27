from sentence_transformers import util
from services.embedder import create_embeddings


def calculate_relevance(question, chunks):

    if not chunks:
        return 0.0


    question_embedding = create_embeddings(
        [question]
    )


    chunk_embeddings = create_embeddings(
        chunks
    )


    scores = util.cos_sim(
        question_embedding,
        chunk_embeddings
    )[0]


    return round(
        float(scores.mean()),
        4
    )