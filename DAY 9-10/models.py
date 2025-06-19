import enum
import datetime
import uuid
from sqlalchemy import Column, DateTime, Float, String, Enum, JSON
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class OrderStatus(enum.Enum):
    pending = "pending"
    shipped = "shipped"
    delivered = "delivered"  

class Order(Base):
    __tablename__ = "orders"
    order_id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    customer_id = Column(String(36), nullable=False)
    order_date = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)
    items = Column(JSON, nullable=False)
    total_amount = Column(Float, nullable=False)
    status = Column(Enum(OrderStatus), default=OrderStatus.pending, nullable=False)
    payment_method = Column(String(50), nullable=True)
    shipping_address = Column(String(225), nullable=False)
