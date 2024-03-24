from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.database import get_db
from crud.crud import create_order, get_order, update_order, delete_order
from schemas.schemas import OrderCreate, OrderUpdate, Order

router = APIRouter()


@router.post("/orders/", response_model=Order)
def create_order_endpoint(order: OrderCreate, db: Session = Depends(get_db)):
    return create_order(db=db, order=order)


@router.get("/{order_id}", response_model=Order)
def read_order(order_id: int, db: Session = Depends(get_db)):
    db_order = get_order(db, order_id=order_id)
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return db_order


@router.put("/{order_id}", response_model=Order)
def update_order_endpoint(
    order_id: int, order: OrderUpdate, db: Session = Depends(get_db)
):
    updated_order = update_order(db=db, order_id=order_id, order=order)
    if updated_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return updated_order


@router.delete("/{order_id}", response_model=Order)
def delete_order_endpoint(order_id: int, db: Session = Depends(get_db)):
    db_order = delete_order(db, order_id=order_id)  # Измените вызов функции
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return db_order
