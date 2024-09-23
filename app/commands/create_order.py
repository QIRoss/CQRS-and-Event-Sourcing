import uuid
from datetime import datetime
from app.event_store.event_store import store_event

def create_order(order: dict):
    order_id = str(uuid.uuid4())
    event = {
        "event_type": "OrderCreated",
        "order_id": order_id,
        "data": order,
        "timestamp": datetime.utcnow()
    }
    store_event(event)
    return {"order_id": order_id, "message": "Order created successfully"}
