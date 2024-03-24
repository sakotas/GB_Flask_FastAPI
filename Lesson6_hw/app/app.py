from fastapi import FastAPI
from routers import router_items, router_orders, router_users
from models.database import engine
from models.models import Base
import uvicorn

app = FastAPI(title="Internet Shop API")

app.include_router(router_items.router, prefix="/items", tags=["items"])
app.include_router(router_orders.router, prefix="/orders", tags=["orders"])
app.include_router(router_users.router, prefix="/users", tags=["users"])

if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
