from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
class CartItemCreate(BaseModel):
    product_id: int
    quantity: int = Field(default=1, ge=1)
class CartItemUpdate(BaseModel):
    quantity: int = Field(..., ge=0)
class CartItemResponse(BaseModel):
    id: int
    user_id: int
    product_id: int
    quantity: int
    created_at: datetime
    
    class Config:
        from_attributes = True