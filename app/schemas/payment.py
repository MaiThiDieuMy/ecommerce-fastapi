from pydantic import BaseModel
from datetime import datetime
from typing import Optional
class PaymentCreate(BaseModel):
    order_id: int
    payment_method: str
    amount: float
class PaymentResponse(BaseModel):
    id: int
    order_id: int
    amount: float
    payment_method: str
    transaction_id: Optional[str] = None
    status: str
    created_at: datetime
    class Config:
        from_attributes = True