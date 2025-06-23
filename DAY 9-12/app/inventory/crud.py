from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.models import Inventory

def create_inventory(db: Session, stock: int) -> Inventory:
    inv = Inventory(stock=stock)
    db.add(inv); db.commit(); db.refresh(inv)
    return inv

def get_inventory(db: Session, product_id: int) -> Inventory:
    inv = db.query(Inventory).get(product_id)
    if not inv:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            f"Product {product_id} not found")
    return inv

def list_inventory(db: Session):
    return db.query(Inventory).all()

def update_inventory(db: Session, product_id: int, stock: int) -> Inventory:
    inv = get_inventory(db, product_id)
    inv.stock = stock
    db.commit(); db.refresh(inv)
    return inv

def delete_inventory(db: Session, product_id: int):
    inv = get_inventory(db, product_id)
    db.delete(inv); db.commit()