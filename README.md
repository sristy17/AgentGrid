# AgentGrid — Autonomous Business Ops AI

AgentGrid is a multi-agent AI backend system that analyzes business data and generates actionable insights and strategies automatically.

It simulates a team of AI “employees” working together — from data processing to decision-making.

---

## Overview

AgentGrid takes business data (JSON or CSV), processes it through a structured pipeline of agents, and returns:

* **Analytics** (revenue, cost, profit)
* **Insights** (problems + reasons, including trend-aware analysis)
* **Strategies** (pricing, growth, cost-cutting)

---

## How It Works

The system follows a multi-agent architecture:

* **Data Agent**
  Ingests and normalizes input data

* **Analytics Agent**
  Computes key business metrics (revenue, cost, profit)

* **Insight Agent (LLM)**
  Analyzes current data along with historical trends to identify problems and reasons

* **Strategy Agent (LLM)**
  Generates actionable business strategies based on insights

* **Orchestrator**
  Coordinates the pipeline, applies guardrails, validation, logging, and integrates historical context

---

## Key Features

* Multi-agent AI system
* FastAPI backend
* Local LLM integration (via Ollama)
* JSON + CSV input support
* Input validation (Pydantic)
* Output validation
* Logging for pipeline tracking
* Guardrails for edge cases (e.g., zero revenue)
* Robust JSON parsing for LLM outputs
* Historical data storage and retrieval using PostgreSQL
* Trend-aware insights using previous analysis runs
* Hybrid architecture (deterministic calculations + AI reasoning)

---

## Tech Stack

* **Backend:** FastAPI
* **Language:** Python
* **LLM Runtime:** Ollama (llama3 / phi)
* **Data Processing:** Pandas
* **Validation:** Pydantic
* **Database:** PostgreSQL
* **ORM:** SQLAlchemy

---

## What This Project Demonstrates

* Multi-agent system design
* LLM integration in backend systems
* Hybrid architecture (deterministic + AI reasoning)
* Stateful AI systems using historical context
* Real-world AI reliability techniques (guardrails, validation, parsing)
* Separation of concerns (logic vs reasoning)
