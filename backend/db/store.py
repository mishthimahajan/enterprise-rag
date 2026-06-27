# import faiss
# import numpy as np


# # FAISS index
# faiss_index = None

# # Store original chunks for citations
# documents = []


# def add_documents(chunks, embeddings):
#     """
#     Add document chunks and their embeddings to FAISS
#     """

#     global faiss_index
#     global documents


#     vectors = np.array(
#         embeddings,
#         dtype="float32"
#     )


#     # Create FAISS index first time
#     if faiss_index is None:

#         dimension = vectors.shape[1]

#         faiss_index = faiss.IndexFlatL2(
#             dimension
#         )


#     # Add vectors to FAISS
#     faiss_index.add(vectors)


#     # Save text chunks
#     documents.extend(chunks)



# def search(query_embedding, k=3):
#     """
#     Semantic search in FAISS
#     """

#     global faiss_index
#     global documents


#     if faiss_index is None:
#         return []


#     query_vector = np.array(
#         query_embedding,
#         dtype="float32"
#     )


#     distances, indices = faiss_index.search(
#         query_vector,
#         k
#     )


#     results = []


#     for idx in indices[0]:

#         if idx >= 0 and idx < len(documents):

#             results.append(
#                 documents[idx]
#             )


#     return results

import os
import pickle
import faiss
import numpy as np

from config import (
    INDEX_FILE,
    METADATA_FILE,
    FAISS_DIR
)


# Embedding dimension for all-MiniLM-L6-v2
DIMENSION = 384


# Create FAISS index using cosine similarity
index = faiss.IndexFlatIP(DIMENSION)


# Store document metadata
documents = []


# ===============================
# Load existing FAISS database
# ===============================
def load_index():

    global index, documents

    try:
        if os.path.exists(INDEX_FILE):

            index = faiss.read_index(
                INDEX_FILE
            )

            print(
                f"Loaded FAISS index with {index.ntotal} vectors"
            )


        if os.path.exists(METADATA_FILE):

            with open(
                METADATA_FILE,
                "rb"
            ) as file:

                documents = pickle.load(file)

            print(
                f"Loaded {len(documents)} documents"
            )

    except Exception as e:

        print(
            "Error loading FAISS database:",
            e
        )

        print(
            "Creating a new FAISS index..."
        )

        index = faiss.IndexFlatIP(DIMENSION)
        documents = []


# ===============================
# Save FAISS database
# ===============================
def save_index():

    os.makedirs(
        FAISS_DIR,
        exist_ok=True
    )


    faiss.write_index(
        index,
        INDEX_FILE
    )


    with open(
        METADATA_FILE,
        "wb"
    ) as file:

        pickle.dump(
            documents,
            file
        )


# ===============================
# Add document chunks
# ===============================
def add_documents(
    chunks,
    embeddings,
    filename
):

    global documents


    metadata = []


    start_id = len(documents)


    for i, chunk in enumerate(chunks):

        metadata.append(
            {
                "id": start_id + i,

                "filename": filename,

                # Later we will store real PDF pages
                "page": 1,

                "text": chunk
            }
        )


    vectors = np.array(
        embeddings,
        dtype="float32"
    )


    index.add(
        vectors
    )


    documents.extend(
        metadata
    )


    save_index()


    print(
        f"Added {len(chunks)} chunks from {filename}"
    )


# ===============================
# Semantic similarity search
# ===============================
def search(
    query_embedding,
    k=5
):

    if index.ntotal == 0:

        return []


    query_vector = np.array(
        query_embedding,
        dtype="float32"
    )


    scores, indices = index.search(
        query_vector,
        k
    )


    results = []


    # Prevent duplicate chunks
    seen = set()


    for score, idx in zip(
        scores[0],
        indices[0]
    ):

        if idx == -1:
            continue


        data = documents[idx]


        # Unique identifier for a chunk
        unique_key = (
            data["filename"],
            data["page"],
            data["text"][:100]
        )


        # Skip repeated chunks
        if unique_key in seen:
            continue


        seen.add(unique_key)


        results.append(
            {
                "text": data["text"],

                "filename": data["filename"],

                "page": data["page"],

                "score": round(
                    float(score) * 100,
                    2
                )
            }
        )


    return results


# ===============================
# Load FAISS on server startup
# ===============================
load_index()