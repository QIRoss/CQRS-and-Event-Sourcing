from app.event_store.event_store import get_events_by_order_id

def get_order_details(order_id: str):
    events = get_events_by_order_id(order_id)
    if not events:
        return {"message": "Order not found"}
    
    order_state = {}
    for event in events:
        if event["event_type"] == "OrderCreated":
            order_state = event["data"]
            order_state["order_id"] = order_id
        elif event["event_type"] == "OrderStatusUpdated":
            order_state["status"] = event["data"]["new_status"]

    return order_state
