import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def create_embeddings(texts):

    if isinstance(texts, str):
        texts = [texts]

    embeddings = []

    for text in texts:

        response = client.models.embed_content(
            model="text-embedding-004",
            contents=text
        )

        embeddings.append(response.embedding.values)

    return embeddings