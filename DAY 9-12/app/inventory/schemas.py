from pydantic import BaseModel, PositiveInt, Field

class InventoryCreate(BaseModel):
    stock: PositiveInt = Field(..., example=100)

class InventoryUpdate(BaseModel):
    stock: PositiveInt = Field(..., example=80)

class InventoryResponse(BaseModel):
    product_id: int
    stock: int

    class Config:
        orm_mode = True