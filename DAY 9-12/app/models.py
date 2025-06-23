import enum
import datetime
from sqlalchemy import (
    Column,
    DateTime,
    Float,
    String,
    Enum,
    JSON,
    Integer,
)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# ────────── Inventory ──────────
class Inventory(Base):
    __tablename__ = "inventory"
    product_id = Column(
        Integer, primary_key=True, autoincrement=True, index=True
    )
    stock = Column(
        Integer, nullable=False, comment="Units in stock"
    )

# ────────── Orders ──────────
class OrderStatus(enum.Enum):
    pending   = "pending"
    shipped   = "shipped"
    delivered = "delivered"

class Order(Base):
    __tablename__ = "orders"

    order_id         = Column(
        Integer, primary_key=True, autoincrement=True, index=True
    )
    customer_id      = Column(
        Integer, nullable=False, index=True
    )
    order_date       = Column(
        DateTime,
        default=datetime.datetime.utcnow,
        nullable=False
    )
    items            = Column(
        JSON, nullable=False,
        comment="[{product_id, name, qty, price}, …]"
    )
    total_amount     = Column(
        Float, nullable=False
    )
    status           = Column(
        Enum(OrderStatus),
        default=OrderStatus.pending,
        nullable=False
    )
    payment_method   = Column(
        String(50), nullable=True
    )
    shipping_address = Column(
        String(255), nullable=False
    )