from app.event_store.event_store import get_all_events

def list_orders():
    events = get_all_events()
    orders = {}

    for event in events:
        order_id = event.get("order_id")
        if not order_id:
            continue

        if event["event_type"] == "OrderCreated":
            orders[order_id] = event["data"]
            orders[order_id]["order_id"] = order_id
        elif event["event_type"] == "OrderStatusUpdated":
            if "status" not in orders[order_id]:
                orders[order_id]["status"] = event["data"]["new_status"]
            else:
                orders[order_id]["status"] = event["data"]["new_status"]

    return list(orders.values())
