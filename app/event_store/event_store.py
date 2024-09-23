from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient("mongodb://mongo:27017/")
db = client["cqrs_db"]
event_collection = db["events"]

def store_event(event: dict):
    event_collection.insert_one(event)

def get_events_by_order_id(order_id: str):
    return list(event_collection.find({"order_id": order_id}))

def get_all_events():
    return list(event_collection.find())
