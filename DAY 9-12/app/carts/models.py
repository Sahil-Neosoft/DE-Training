import datetime
from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from app.models import Base

class Cart(Base):
    __tablename__ = "carts"
    cart_id     = Column(Integer, primary_key=True,
                         index=True, autoincrement=True)
    customer_id = Column(Integer, nullable=False, index=True)
    created_at  = Column(DateTime, default=datetime.datetime.utcnow)

    items = relationship("CartItem",
                         back_populates="cart",
                         cascade="all, delete-orphan")

class CartItem(Base):
    __tablename__ = "cart_items"
    id         = Column(Integer, primary_key=True,
                        index=True, autoincrement=True)
    cart_id    = Column(Integer,
                        ForeignKey("carts.cart_id",
                                   ondelete="CASCADE"))
    product_id = Column(Integer, nullable=False)
    quantity   = Column(Integer, nullable=False)

    cart = relationship("Cart", back_populates="items")