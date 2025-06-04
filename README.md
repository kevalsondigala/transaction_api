# Transaction API

A FastAPI + SQLite backend to ingest user transactions and return monthly spending summaries.

---

## Features

- Ingest transaction data
- Monthly summary by category
- Bearer token auth
- SQLite database
- Dockerized & tested

---

## Auth

All endpoints require:

---

## POST /ingest

Ingest transaction(s):

```json
[
  {
    "user_id": "user_123",
    "amount": 100.0,
    "category": "Groceries",
    "narration": "UPI TXN",
    "timestamp": "2024-12-01T10:00:00Z"
  }
]
```
## GET /summary
/summary?user_id=user_123&month=2024-12

```json
{
  "user_id": "user_123",
  "month": "2024-12",
  "total_spent": 100.0,
  "category_breakdown": {
    "Groceries": 100.0
  }
}
```

## Run
```bash
uvicorn app.main:app --reload
    OR with Docker
docker build -t transaction-api .
docker run -p 8000:8000 transaction-api
```

## Test
```bash
pytest tests/
```