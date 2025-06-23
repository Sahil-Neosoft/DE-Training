from pydantic import BaseModel, PositiveInt, Field
from typing import List
from datetime import datetime

class OrderItem(BaseModel):
    product_id: PositiveInt
    name: str = Field(..., min_length=2, max_length=100)
    quantity