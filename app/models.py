from sqlalchemy import Column, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
import uuid

Base = declarative_base()

class Transaction(Base):
    __tablename__ = 'transactions'
    
    transaction_id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String, index=True)
    amount = Column(Float)
    category = Column(String)
    narration = Column(String)
    timestamp = Column(DateTime)
