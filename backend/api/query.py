from fastapi import APIRouter
from pydantic import BaseModel

from services.embedder import create_embeddings
from services.llm import generate_answer
from db.store import search
from memory.chat_memory import memory
from evaluation.latency import (
    start_timer,
    end_timer
)

router = APIRouter()


class QueryRequest(BaseModel):
    question: str
    session_id: str


@router.post("/query")
async def query_documents(request: QueryRequest):

    timer = start_timer()

    question = request.question.strip()

    memory.add_message(
        request.session_id,
        "user",
        question
    )

    if not question:
        return {
            "answer": "Please enter a valid question.",
            "sources": [],
            "evaluation": {}
        }

    # Create query embedding
    query_embedding = create_embeddings([question])

    # Search FAISS
    results = search(
        query_embedding,
        k=3
    )

    if not results:

        response_time = end_timer(timer)

        return {
            "answer": "No relevant information found.",
            "sources": [],
            "evaluation": {
                "retrieval_relevance": 0.0,
                "answer_faithfulness": 0.0,
                "response_time_seconds": response_time
            }
        }

    retrieved_chunks = [
        item["text"]
        for item in results
    ]

    # Disable evaluation temporarily
    relevance_score = 0.0

    context = "\n\n".join(
        retrieved_chunks
    )

    history = memory.get_history(
        request.session_id
    )

    chat_history = "\n".join(
        [
            f"{msg['role']}: {msg['content']}"
            for msg in history
        ]
    )

    full_context = f"""
Conversation History:
{chat_history}

Document Context:
{context}
"""

    answer = generate_answer(
        question,
        full_context
    )

    memory.add_message(
        request.session_id,
        "assistant",
        answer
    )

    # Disable evaluation temporarily
    faithfulness_score = 0.0

    response_time = end_timer(timer)

    return {
        "answer": answer,
        "sources": results,
        "evaluation": {
            "retrieval_relevance": relevance_score,
            "answer_faithfulness": faithfulness_score,
            "response_time_seconds": response_time
        }
    }