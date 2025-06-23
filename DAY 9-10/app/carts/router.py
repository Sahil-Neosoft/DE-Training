from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.carts import crud, schemas

router = APIRouter(tags=["Carts"])

@router.post("/", response_model=schemas.CartResponse, status_code=status.HTTP_201_CREATED)
def create_cart(cart_in: schemas.CartCreate, db: Session = Depends(get_db)):
    return crud.create_cart(db, cart_in)

@router.get("/{cart_id}", response_model=schemas.CartResponse)
def get_cart(cart_id: int, db: Session = Depends(get_db)):
    return crud.get_cart(db, cart_id)

@router.post("/{cart_id}/items", response_model=schemas.CartItemResponse)
def add_item_to_cart(cart_id: int, item_in: schemas.CartItemCreate, db: Session = Depends(get_db)):
    return crud.add_item(db, cart_id, item_in)

@router.get("/{cart_id}/items", response_model=list[schemas.CartItemResponse])
def list_items(cart_id: int, db: Session = Depends(get_db)):
    return crud.list_cart_items(db, cart_id)

@router.put("/{cart_id}/items/{product_id}", response_model=schemas.CartItemResponse)
def update_item(cart_id: int, product_id: int, quantity: int, db: Session = Depends(get_db)):
    return crud.update_item_quantity(db, cart_id, product_id, quantity)

@router.delete("/{cart_id}/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_item(cart_id: int, item_id: int, db: Session = Depends(get_db)):
    crud.remove_item(db, item_id)

@router.delete("/{cart_id}/clear", status_code=status.HTTP_204_NO_CONTENT)
def clear_cart(cart_id: int, db: Session = Depends(get_db)):
    crud.clear_cart(db, cart_id)