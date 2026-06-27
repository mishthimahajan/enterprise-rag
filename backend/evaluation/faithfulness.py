from sentence_transformers import util
from services.embedder import create_embeddings


def calculate_faithfulness(answer, context):
    """
    Measures how much the answer
    matches the retrieved context
    """

    if not answer or not context:
        return 0.0


    answer_embedding = create_embeddings(
        [answer]
    )


    context_embedding = create_embeddings(
        [context]
    )


    score = util.cos_sim(
        answer_embedding,
        context_embedding
    )


    return round(
        score.item(),
        4
    )