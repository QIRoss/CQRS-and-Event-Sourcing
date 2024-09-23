from fastapi import FastAPI
from app.commands.create_order import create_order
from app.commands.update_order_status import update_order_status
from app.queries.get_order_details import get_order_details
from app.queries.list_orders import list_orders

app = FastAPI()

@app.post("/orders/")
async def create_order_endpoint(order: dict):
    return create_order(order)

@app.put("/orders/{order_id}/status/")
async def update_order_status_endpoint(order_id: str, status: dict):
    return update_order_status(order_id, status['new_status'])

@app.get("/orders/{order_id}/")
async def get_order_details_endpoint(order_id: str):
    return get_order_details(order_id)

@app.get("/orders/")
async def list_orders_endpoint():
    return list_orders()
