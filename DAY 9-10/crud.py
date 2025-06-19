from typing import List
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

import models
import schemas


def create_order(db: Session, order_in: schemas.OrderCreate) -> models.Order:
    total = sum(item.quantity * item.price for item in order_in.items)

    safe_items = [
        {
            **item.model_dump(),                  
            "product_id": str(item.product_id),  
        }
        for item in order_in.items
    ]

    db_order = models.Order(
        customer_id=str(order_in.customer_id),  
        items=safe_items,
        payment_method=order_in.payment_method,
        shipping_address=order_in.shipping_address,
        total_amount=total
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order


def get_order(db: Session, order_id: str) -> models.Order:
    order = db.query(models.Order) \
              .filter(models.Order.order_id == order_id) \
              .first()
    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Order {order_id} not found"
        )
    return order


def list_orders(db: Session) -> List[models.Order]:

    return db.query(models.Order).all()


def update_order_status(db: Session,order_id: str,status_str: str) -> models.Order:
    order = get_order(db, order_id)

    try:
        order.status = models.OrderStatus(status_str)
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid status '{status_str}'"
        )

    db.commit()
    db.refresh(order)
    return order