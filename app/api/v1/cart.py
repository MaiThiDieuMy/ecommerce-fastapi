from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.schemas.cart import CartItemCreate, CartItemUpdate, CartItemResponse
from app.services import cart_service
router = APIRouter(tags=['Cart'])
# Mock user_id for workshop (normally from JWT)
MOCK_USER_ID = 1
@router.get('/cart', response_model=List[CartItemResponse])
def get_cart(db: Session = Depends(get_db)):
    return cart_service.get_cart(db, user_id=MOCK_USER_ID)
@router.post('/cart', response_model=CartItemResponse, status_code=status.HTTP_201_CREATED)
def add_to_cart(item: CartItemCreate, db: Session = Depends(get_db)):
    result = cart_service.add_to_cart(db, user_id=MOCK_USER_ID, cart_item=item)
    if not result:
        raise HTTPException(status_code=404, detail='Product not found')
    return result
@router.put('/cart/{item_id}', response_model=CartItemResponse)
def update_cart_item(item_id: int, update: CartItemUpdate, db: Session = Depends(get_db)):
    result = cart_service.update_cart_item(db, user_id=MOCK_USER_ID, item_id=item_id, update=update)
    if result is None and update.quantity > 0:
        raise HTTPException(status_code=404, detail='Cart item not found')
    return result
@router.delete('/cart')
def clear_cart(db: Session = Depends(get_db)):
    cart_service.clear_cart(db, user_id=MOCK_USER_ID)
    return {'message': 'Cart cleared'}
    