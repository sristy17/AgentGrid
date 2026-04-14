# AgentGrid — Autonomous Business Ops AI

AgentGrid is a multi-agent AI backend system that analyzes business data and generates actionable insights and strategies automatically.

It simulates a team of AI “employees” working together — from data processing to decision-making.

---

## Overview

AgentGrid takes business data (JSON or CSV), processes it through a structured pipeline of agents, and returns:

* Analytics (revenue, cost, profit)
* Insights (problems + reasons)
* Strategies (pricing, growth, cost-cutting)

---

## How It Works

The system follows a multi-agent architecture:

1. **Data Agent**
   Ingests and normalizes input data.

2. **Analytics Agent**
   Computes key business metrics (revenue, cost, profit).

3. **Insight Agent (LLM)**
   Analyzes the data to identify problems and reasons.

4. **Strategy Agent (LLM)**
   Suggests actionable business strategies.

5. **Orchestrator**
   Coordinates the full pipeline, adds guardrails, validation, and logging.

---

##  Key Features

* Multi-agent AI system
* FastAPI backend
* Local LLM integration (via Ollama)
* JSON + CSV input support
* Input validation (Pydantic)
* Output validation
* Logging for pipeline tracking
* Guardrails for edge cases (e.g., zero revenue)
* Robust JSON parsing for LLM outputs



##  Tech Stack

* **Backend:** FastAPI
* **Language:** Python
* **LLM Runtime:** Ollama (local models like llama3 / phi)
* **Data Processing:** Pandas
* **Validation:** Pydantic




## What This Project Demonstrates

* Multi-agent system design
* LLM integration in backend systems
* Hybrid architecture (deterministic + AI reasoning)
* Real-world AI reliability techniques (guardrails, validation, parsing)

