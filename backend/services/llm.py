import os

from google import genai
from dotenv import load_dotenv


# Load environment variables
load_dotenv()


# Create Gemini client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_answer(question, context):

    prompt = f"""
You are an Enterprise RAG Assistant.

Your task:
- Answer only using the provided document context.
- Give concise and professional answers.
- If information is missing, say "I could not find this in the uploaded documents."
- Do not make up information.
- Summarize the answer clearly.

Context:
{context}

Question:
{question}

Answer:
"""

   

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=prompt
        )

        return response.text

    except Exception as e:
        print("GEMINI ERROR:", e)

        return f"Gemini Error: {str(e)}"
