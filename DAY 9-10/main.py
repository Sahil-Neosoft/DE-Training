from fastapi import (
    FastAPI, Depends, Body, Path
)
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional
import uuid
from faker import Faker

import models, schemas, crud

from db import engine
from dependencies import get_db
from middleware import log_errors
from exceptions import custom_exception_handler

# auto-create tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="E-commerce Orders API",
    version="1.0.0",
    description="Create, Read, list and update orders"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# error‐logging middleware & handler
app.middleware("http")(log_errors)
app.add_exception_handler(Exception, custom_exception_handler)

faker = Faker()

@app.post(
    "/orders/",
    response_model=List[schemas.OrderResponse],
    tags=["Orders"],
)
def create_orders(
    order: Optional[schemas.OrderCreate] = Body(None),
    db=Depends(get_db)
):
    created = []
    if order:
        created.append(crud.create_order(db, order))
    else:
        for _ in range(faker.random_int(1, 5)):
            items = [
                schemas.Item(
                    product_id=uuid.uuid4(),
                    name=faker.pystr(min_chars=2, max_chars=100),
                    quantity=faker.random_int(1, 5),
                    price=round(faker.random_number(3) + faker.random.random(), 2)
                )
                for __ in range(faker.random_int(1, 4))
            ]   
            fake_order = schemas.OrderCreate(
                customer_id=uuid.uuid4(),
                items=items,
                payment_method=faker.random_element(["credit_card", "paypal", "upi"]),
                shipping_address=faker.address()
            )
            created.append(crud.create_order(db, fake_order))
    return created


@app.get(
    "/orders/",
    response_model=List[schemas.OrderResponse],
    tags=["Orders"],
)
def read_orders(db=Depends(get_db)):
    return crud.list_orders(db)


@app.get(
    "/orders/{order_id}",
    response_model=schemas.OrderResponse,
    tags=["Orders"],
)
def read_order(
    order_id: str = Path(..., description="UUID of the order"),
    db=Depends(get_db)
):
    return crud.get_order(db, order_id)


@app.put(
    "/orders/{order_id}/status",
    response_model=schemas.OrderResponse,
    tags=["Orders"],
)
def change_status(
    order_id: str = Path(..., description="UUID of the order"),
    status: str = Body(..., description="New status"),
    db=Depends(get_db)
):
    return crud.update_order_status(db, order_id, status)