from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.schemas.order import OrderCreate, OrderResponse
from app.services import order_service
router = APIRouter(tags=['Orders'])
MOCK_USER_ID = 1
@router.post('/orders', response_model=OrderResponse, status_code=status.HTTP_201_CREATED)
def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    result = order_service.create_order_from_cart(db, user_id=MOCK_USER_ID, order_data=order)
    if not result:
        raise HTTPException(status_code=400, detail='Cart is empty')
    return result
@router.get('/orders', response_model=List[OrderResponse])
def get_orders(db: Session = Depends(get_db)):
    return order_service.get_user_orders(db, user_id=MOCK_USER_ID)
@router.get('/orders/{order_id}', response_model=OrderResponse)
def get_order(order_id: int, db: Session = Depends(get_db)):
    order = order_service.get_order(db, order_id=order_id, user_id=MOCK_USER_ID)
    if not order:
        raise HTTPException(status_code=404, detail='Order not found')
    return order