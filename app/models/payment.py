from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import enum
from app.database import Base
class PaymentStatus(str, enum.Enum):
    PENDING = 'pending'
    COMPLETED = 'completed'
    FAILED = 'failed'
    REFUNDED = 'refunded'
class Payment(Base):
    __tablename__ = 'payments'
    
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    amount = Column(Float, nullable=False)
    payment_method = Column(String(50))
    transaction_id = Column(String(200))
    status = Column(Enum(PaymentStatus), default=PaymentStatus.PENDING)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationship
    order = relationship('Order')