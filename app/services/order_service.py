from sqlalchemy.orm import Session
from app.models.order import Order, OrderItem, OrderStatus
from app.models.cart import CartItem
from app.schemas.order import OrderCreate
def create_order_from_cart(db: Session, user_id: int, order_data: OrderCreate):
    # Get cart items
    cart_items = db.query(CartItem).filter(CartItem.user_id == user_id).all()
    
    if not cart_items:
        return None
    
    # Calculate total
    total_amount = sum(item.product.price * item.quantity for item in cart_items)
    
    # Create order
    db_order = Order(
        user_id=user_id,
        total_amount=total_amount,
        shipping_address=order_data.shipping_address,
        status=OrderStatus.PENDING
    )
    db.add(db_order)
    db.flush()  # Get order ID
    
    # Create order items
    for cart_item in cart_items:
        order_item = OrderItem(
            order_id=db_order.id,
            product_id=cart_item.product_id,
            quantity=cart_item.quantity,
            price=cart_item.product.price  # Snapshot price
        )
        db.add(order_item)
    
    # Clear cart
    db.query(CartItem).filter(CartItem.user_id == user_id).delete()
    
    db.commit()
    db.refresh(db_order)
    return db_order
def get_user_orders(db: Session, user_id: int):
    return db.query(Order).filter(Order.user_id == user_id).all()
def get_order(db: Session, order_id: int, user_id: int):
    return db.query(Order).filter(
        Order.id == order_id,
        Order.user_id == user_id
    ).first()