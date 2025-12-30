from pydantic import BaseModel, Field
from datetime import datetime
from typing import List, Optional
class OrderItemCreate(BaseModel):
    product_id: int
    quantity: int
    price: float
class OrderItemResponse(BaseModel):
    id: int
    product_id: int
    quantity: int
    price: float
    
    class Config:
        from_attributes = True
class OrderCreate(BaseModel):
    shipping_address: str = Field(..., min_length=10)
class OrderResponse(BaseModel):
    id: int
    user_id: int
    total_amount: float
    status: str
    shipping_address: str
    created_at: datetime
    items: List[OrderItemResponse] = []
    
    class Config:
        from_attributes = True