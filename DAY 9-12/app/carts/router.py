from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.carts import crud, schemas

router = APIRouter(prefix="/carts", tags=["Carts"])

@router.post("/", response_model=schemas.CartResponse)
def api_create_cart(cart: schemas.CartCreate,
                    db: Session = Depends(get_db)):
    return crud.create_cart(db, cart)

@router.get("/{cart_id}", response_model=schemas.CartResponse)
def api_get_cart(cart_id: int,
                 db: Session = Depends(get_db)):
    return crud.get_cart(db, cart_id)

@router.post("/{cart_id}/items",
             response_model=schemas.CartItemResponse)
def api_add_item(cart_id: int,
                 item: schemas.CartItemCreate,
                 db: Session = Depends(get_db)):
    return crud.add_item(db, cart_id, item)

@router.delete("/items/{item_id}")
def api_remove_item(item_id: int,
                    db: Session = Depends(get_db)):
    crud.remove_item(db, item_id)
    return {"detail": "Item removed"}

@router.delete("/{cart_id}/items")
def api_clear_cart(cart_id: int,
                   db: Session = Depends(get_db)):
    crud.clear_cart(db, cart_id)
    return {"detail": "Cart cleared"}