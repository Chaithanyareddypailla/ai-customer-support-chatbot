# **AI Customer Support Chatbot**

An AI-powered customer support chatbot built using FastAPI, Retrieval-Augmented Generation (RAG), Redis memory, Prometheus metrics, and local LLMs via Ollama.
The system provides context-aware responses, conversation memory, and production-grade observability — all without relying on paid APIs.

## Project Overview
This project demonstrates how to build a production-style AI customer support system that:
- Answers customer questions using enterprise knowledge (RAG)
- Maintains conversation history per user using Redis
- Uses local LLMs (Ollama) — no OpenAI API or billing required
- Exposes Prometheus-compatible metrics for monitoring
- Is built using FastAPI, following real backend best practices
This architecture mirrors how modern AI SaaS platforms are designed.

---
## Tech Stack

| **Component**    | **Technology**               |
| ---------------- | ---------------------------- |
| Backend API      | FastAPI                      |
| LLM              | Ollama (phi3:mini / mistral) |
| RAG              | Vector similarity search     |
| Memory           | Redis                        |
| Metrics          | Prometheus                   |
| Language         | Python 3.13                  |
| Deployment Style | Local / Cloud-ready          |

---

## Key Features
- Context-aware answers using RAG
- User-level memory with Redis
- Free local AI inference using Ollama
- Production metrics with Prometheus
- Clean API design with FastAPI
