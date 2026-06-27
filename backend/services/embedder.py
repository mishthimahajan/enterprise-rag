# from sentence_transformers import SentenceTransformer

# model = SentenceTransformer(
#     "all-MiniLM-L6-v2"
# )


# def create_embeddings(texts):

#     return model.encode(
#         texts,
#         convert_to_numpy=True
#     )

from sentence_transformers import (
    SentenceTransformer
)


MODEL = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def create_embeddings(texts):

    embeddings = MODEL.encode(
        texts,
        convert_to_numpy=True,
        normalize_embeddings=True
    )

    return embeddings