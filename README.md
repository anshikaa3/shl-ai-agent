# SHL AI Assessment Recommendation Agent

## Overview

This project is a conversational AI agent that recommends relevant SHL assessments based on hiring requirements.

The system supports:

- Conversational recommendation flow
- Context-aware refinement handling
- SHL assessment retrieval
- REST APIs using FastAPI
- Public deployment using Render

The application accepts hiring requirements as input and returns recommended SHL assessments with URLs.

---

# Features

- Conversational AI-style interaction
- Multi-turn refinement support
- SHL assessment recommendation engine
- Lightweight keyword-based retrieval
- FastAPI backend
- Swagger API documentation
- Public cloud deployment
- Health monitoring endpoint

---

# Tech Stack

## Backend

- Python
- FastAPI
- Uvicorn

## Data Collection

- Selenium
- BeautifulSoup
- Requests

## Retrieval

- JSON-based lightweight retrieval system

## Deployment

- Render

---

# Project Structure

```text
shl-ai-agent/
│
├── app/
│   ├── main.py
│   ├── agent.py
│   ├── retriever.py
│   ├── scraper.py
│   └── models.py
│
├── catalog.json
├── catalog_detailed.json
├── requirements.txt
├── Procfile
├── README.md
└── .gitignore
```

---

# API Endpoints

## 1. Health Endpoint

### Request

```http
GET /health
```

### Response

```json
{
  "status": "ok"
}
```

---

## 2. Chat Endpoint

### Request

```http
POST /chat
```

### Sample Request Body

```json
{
  "messages": [
    {
      "role": "user",
      "content": "Hiring Java developer with communication skills"
    }
  ]
}
```

### Sample Response

```json
{
  "reply": "Based on the updated hiring requirements, these SHL assessments may be relevant...",
  "recommendations": [
    {
      "name": "Assessment Name",
      "url": "https://www.shl.com/"
    }
  ],
  "end_of_conversation": false
}
```

---

# Conversational Refinement Support

The system supports multi-turn conversation refinement.

Example:

### User

```text
Hiring Java developer
```

### User Refinement

```text
Also include personality assessments
```

The agent combines conversation history to improve recommendations.

---

# Data Collection

The SHL product catalog was scraped using:

- Selenium
- BeautifulSoup

Assessment metadata is stored locally in:

- `catalog.json`
- `catalog_detailed.json`

---

# Recommendation Logic

The recommendation engine uses:

- keyword matching
- scoring based on hiring requirement overlap
- lightweight retrieval for fast deployment

---

# Local Setup

## 1. Clone Repository

```bash
git clone https://github.com/anshikaa3/shl-ai-agent.git
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

---

## 3. Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

---

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 5. Run Application

```bash
uvicorn app.main:app --reload
```

---

# Deployment

The application is deployed publicly on Render.

## Live API

https://shl-ai-agent-kkqm.onrender.com

---

## Swagger API Docs

https://shl-ai-agent-kkqm.onrender.com/docs

---

# GitHub Repository

https://github.com/anshikaa3/shl-ai-agent

---

# Future Improvements

- Better semantic retrieval
- Larger SHL catalog coverage
- Vector database integration
- Improved ranking logic
- Frontend UI integration
- LLM-powered conversational ranking

---

# Author

Anshika Srivastava
