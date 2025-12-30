from sqlalchemy.orm import Session
from app.models.cart import CartItem
from app.models.product import Product
from app.schemas.cart import CartItemCreate, CartItemUpdate
def get_cart(db: Session, user_id: int):
    return db.query(CartItem).filter(CartItem.user_id == user_id).all()
def add_to_cart(db: Session, user_id: int, cart_item: CartItemCreate):
    # Check if product exists
    product = db.query(Product).filter(Product.id == cart_item.product_id).first()
    if not product:
        return None
    
    # Check if item already in cart
    existing = db.query(CartItem).filter(
        CartItem.user_id == user_id,
        CartItem.product_id == cart_item.product_id
    ).first()
    
    if existing:
        # Update quantity
        existing.quantity += cart_item.quantity
        db.commit()
        db.refresh(existing)
        return existing
    else:
        # Create new cart item
        db_item = CartItem(
            user_id=user_id,
            product_id=cart_item.product_id,
            quantity=cart_item.quantity
        )
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item
def update_cart_item(db: Session, user_id: int, item_id: int, update: CartItemUpdate):
    db_item = db.query(CartItem).filter(
        CartItem.id == item_id,
        CartItem.user_id == user_id
    ).first()
    
    if not db_item:
        return None
    
    if update.quantity == 0:
        # Remove from cart
        db.delete(db_item)
        db.commit()
        return None
    else:
        db_item.quantity = update.quantity
        db.commit()
        db.refresh(db_item)
        return db_item
def clear_cart(db: Session, user_id: int):
    db.query(CartItem).filter(CartItem.user_id == user_id).delete()
    db.commit()