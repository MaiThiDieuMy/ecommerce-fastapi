from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.payment import PaymentCreate, PaymentResponse
from app.services import payment_service
router = APIRouter(tags=['Payment'])
@router.post('/payments', response_model=PaymentResponse, status_code=status.HTTP_201_CREATED)
def process_payment(payment: PaymentCreate, db: Session = Depends(get_db)):
    result = payment_service.process_payment(db, payment)
    if result.status == 'failed':
        raise HTTPException(status_code=400, detail='Payment failed')
    return result
@router.get('/payments/{payment_id}', response_model=PaymentResponse)
def get_payment(payment_id: int, db: Session = Depends(get_db)):
    payment = payment_service.get_payment(db, payment_id)
    if not payment:
        raise HTTPException(status_code=404, detail='Payment not found')
    return payment