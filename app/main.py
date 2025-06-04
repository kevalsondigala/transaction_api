from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas import TransactionIn, TransactionSummary
from database import SessionLocal, init_db
from crud import add_transactions, get_summary
from auth import authenticate
from typing import List

app = FastAPI()

init_db()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/ingest")
def ingest(transactions: List[TransactionIn], db: Session = Depends(get_db), _: str = Depends(authenticate)):
    added = add_transactions(db, transactions)
    return {"status": "success", "added": len(added)}

@app.get("/summary", response_model=TransactionSummary)
def summary(user_id: str, month: str, db: Session = Depends(get_db), _: str = Depends(authenticate)):
    return get_summary(db, user_id, month)
