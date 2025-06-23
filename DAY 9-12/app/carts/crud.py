from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.carts.models import Cart, CartItem
from app.models import Inventory
from app.carts.schemas import CartCreate, CartItemCreate

def create_cart(db: Session, cart_in: CartCreate) -> Cart:
    cart = Cart(customer_id=cart_in.customer_id)
    db.add(cart); db.commit(); db.refresh(cart)
    return cart

def get_cart(db: Session, cart_id: int) -> Cart:
    cart = db.query(Cart).filter_by(cart_id=cart_id).first()
    if not cart:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            f"Cart {cart_id} not found")
    return cart

def add_item(db: Session, cart_id: int, ci: CartItemCreate) -> CartItem:
    inv = db.query(Inventory).get(ci.product_id)
    if not inv or inv.stock < ci.quantity:
        raise HTTPException(status.HTTP_400_BAD_REQUEST,
                            "Insufficient stock")
    item = db.query(CartItem)\
             .filter_by(cart_id=cart_id,
                        product_id=ci.product_id)\
             .first()
    if item:
        new_qty = item.quantity + ci.quantity
        if inv.stock < new_qty:
            raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                "Insufficient stock for update")
        item.quantity = new_qty
    else:
        item = CartItem(cart_id=cart_id, **ci.dict())
        db.add(item)

    inv.stock -= ci.quantity
    db.commit(); db.refresh(item)
    return item

def remove_item(db: Session, item_id: int):
    item = db.query(CartItem).get(item_id)
    if not item:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            "Cart item not found")
    inv = db.query(Inventory).get(item.product_id)
    inv.stock += item.quantity
    db.delete(item); db.commit()

def clear_cart(db: Session, cart_id: int):
    items = db.query(CartItem).filter_by(cart_id=cart_id).all()
    for it in items:
        inv = db.query(Inventory).get(it.product_id)
        inv.stock += it.quantity
        db.delete(it)
    db.commit()