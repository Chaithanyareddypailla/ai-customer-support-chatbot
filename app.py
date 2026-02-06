from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import Response
import requests

from prometheus_client import generate_latest, CONTENT_TYPE_LATEST
from rag import load_knowledge
from memory import save_message, get_history
from metrics import chat_counter

app = FastAPI()

# Load vector database (RAG)
db = load_knowledge()


# 🔹 Ollama local LLM call (FREE, no API key)
def call_llm(prompt: str) -> str:
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "phi3:mini",   # low-memory friendly model
            "prompt": prompt,
            "stream": False
        },
        timeout=120
    )
    response.raise_for_status()
    return response.json()["response"]


# ✅ ROOT ENDPOINT
@app.get("/")
def root():
    return {"message": "AI Customer Support Chatbot (Ollama) is running 🚀"}


# ✅ PROMETHEUS METRICS ENDPOINT (THIS FIXES 404)
@app.get("/metrics")
def metrics():
    return Response(
        generate_latest(),
        media_type=CONTENT_TYPE_LATEST
    )


# ✅ REQUEST BODY MODEL
class ChatRequest(BaseModel):
    user_id: str
    question: str


# 🤖 CHATBOT ENDPOINT
@app.post("/chat")
def chat(request: ChatRequest):
    chat_counter.inc()

    # Save user message in Redis
    save_message(request.user_id, request.question)
    history = get_history(request.user_id)

    # RAG similarity search
    docs = db.similarity_search(request.question, k=1)

    if not docs:
        return {"answer": "I will connect you to a human agent."}

    prompt = f"""
    Answer the question using the context below.

    Context:
    {docs[0].page_content}

    Question:
    {request.question}
    """

    answer = call_llm(prompt)

    return {
        "answer": answer,
        "previous_messages": history
    }
