from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.inventory import crud, schemas

router = APIRouter(prefix="/inventory", tags=["Inventory"])

@router.post("/", response_model=schemas.InventoryResponse,
             status_code=status.HTTP_201_CREATED)
def create_product(inv_in: schemas.InventoryCreate,
                   db: Session = Depends(get_db)):
    return crud.create_inventory(db, inv_in.stock)

@router.get("/", response_model=list[schemas.InventoryResponse])
def list_products(db: Session = Depends(get_db)):
    return crud.list_inventory(db)

@router.get("/{product_id}", response_model=schemas.InventoryResponse)
def get_product(product_id: int, db: Session = Depends(get_db)):
    return crud.get_inventory(db, product_id)

@router.put("/{product_id}", response_model=schemas.InventoryResponse)
def update_product(product_id: int,
                   inv_in: schemas.InventoryUpdate,
                   db: Session = Depends(get_db)):
    return crud.update_inventory(db, product_id, inv_in.stock)

@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    crud.delete_inventory(db, product_id)