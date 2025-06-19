from pydantic import BaseModel,Field
from typing import List
from datetime import datetime
import uuid

class Item(BaseModel):
    product_id:uuid.UUID
    name:str = Field(...,min_length=2,max_length=100)
    quantity: int = Field(...,gt=0)
    price: float = Field(...,gt=0)

class OrderCreate(BaseModel):
    customer_id: uuid.UUID
    items:List[Item]
    payment_method: str=Field(...,min_length=2,max_length=225)
    shipping_address: str=Field(...,min_length=8,max_length=225)

class OrderResponse(BaseModel):
    order_id:uuid.UUID
    order_date:datetime
    total_amount:float
    status:str  