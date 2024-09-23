from datetime import datetime
from app.event_store.event_store import store_event

def update_order_status(order_id: str, new_status: str):
    event = {
        "event_type": "OrderStatusUpdated",
        "order_id": order_id,
        "data": {"new_status": new_status},
        "timestamp": datetime.utcnow()
    }
    store_event(event)
    return {"order_id": order_id, "message": "Order status updated to {}".format(new_status)}
