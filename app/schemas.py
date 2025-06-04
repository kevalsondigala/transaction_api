from pydantic import BaseModel
from datetime import datetime
from typing import List, Dict

class TransactionIn(BaseModel):
    user_id: str
    amount: float
    category: str
    narration: str
    timestamp: datetime

class TransactionSummary(BaseModel):
    user_id: str
    month: str
    total_spent: float
    category_breakdown: Dict[str, float]
