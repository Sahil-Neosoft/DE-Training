from pydantic import BaseModel, PositiveInt
from typing import List
from datetime import datetime

class CartItemCreate(BaseModel):
    product_id: PositiveInt
    quantity: PositiveInt

class CartItemResponse(CartItemCreate):
    id: int

    class Config:
        orm_mode = True

class CartCreate(BaseModel):
    customer_id: PositiveInt

class CartResponse(CartCreate):
    cart_id: int
    created_at: datetime
    items: List[CartItemResponse]

    class Config:
        orm_mode = True