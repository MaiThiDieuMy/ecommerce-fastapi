from sqlalchemy.orm import Session
from app.models.payment import Payment, PaymentStatus
from app.schemas.payment import PaymentCreate
import random
import string
def process_payment(db: Session, payment_data: PaymentCreate):
    # Simulate payment gateway call
    transaction_id = generate_transaction_id()
    
    # Simulate fail randomly (10% chance for demo)
    import random
    success = random.random() > 0.1
    
    status = PaymentStatus.COMPLETED if success else PaymentStatus.FAILED
    
    db_payment = Payment(
        order_id=payment_data.order_id,
        amount=payment_data.amount,
        payment_method=payment_data.payment_method,
        transaction_id=transaction_id,
        status=status
    )
    db.add(db_payment)
    db.commit()
    db.refresh(db_payment)
    return db_payment
def get_payment(db: Session, payment_id: int):
    return db.query(Payment).filter(Payment.id == payment_id).first()
def generate_transaction_id():
    return 'TXN_' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))