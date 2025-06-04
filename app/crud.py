from sqlalchemy.orm import Session
from models import Transaction
from schemas import TransactionIn
from sqlalchemy import func
from collections import defaultdict

def add_transactions(db: Session, transactions: list[TransactionIn]):
    added = []
    for t in transactions:
        exists = db.query(Transaction).filter_by(user_id=t.user_id, timestamp=t.timestamp, amount=t.amount).first()
        if not exists:
            tx = Transaction(**t.model_dump())
            db.add(tx)
            added.append(tx)
    db.commit()
    return added

def get_summary(db: Session, user_id: str, month: str):
    # month format: "YYYY-MM"
    txns = db.query(Transaction).filter(
        Transaction.user_id == user_id,
        func.strftime('%Y-%m', Transaction.timestamp) == month
    ).all()

    summary = {}
    total = 0.0

    for txn in txns:
        summary[txn.category] = summary.get(txn.category, 0.0) + txn.amount
        total += txn.amount

    return {
        "user_id": user_id,
        "month": month,
        "total_spent": round(total, 2),
        "category_breakdown": {k: round(v, 2) for k, v in summary.items()}
    }

