from pydantic import BaseModel
from typing import List, Optional
import datetime


class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None
    price: float


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int

    class Config:
        from_attributes = True


class ItemUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None


class UserBase(BaseModel):
    name: str
    surname: str
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    items: List[Item] = []

    class Config:
        from_attributes = True


class UserUpdate(BaseModel):
    name: Optional[str] = None
    surname: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None


class OrderBase(BaseModel):
    user_id: int
    item_id: int
    order_date: datetime.datetime
    status: str


class OrderCreate(OrderBase):
    pass


class OrderUpdate(BaseModel):
    user_id: Optional[int] = None
    item_id: Optional[int] = None
    order_date: Optional[datetime.datetime] = None
    status: Optional[str] = None


class Order(OrderBase):
    id: int

    class Config:
        from_attributes = True
