# CQRS and Event Sourcing

Studies based in day 5-6 of 100 Days System Design for DevOps and Cloud Engineers

https://deoshankar.medium.com/100-days-system-design-for-devops-and-cloud-engineers-18af7a80bc6f

Days 1–10: Advanced Architectural Concepts.

Day 5–6: Explore CQRS (Command Query Responsibility Segregation) and Event Sourcing patterns; apply them to a service.

# How This Differs from CRUD

In a traditional CRUD system when you create or update an order, only the current state is stored. For example, when you change an order status from "processing" to "shipped," the "processing" status is overwritten and lost.

In contrast, with Event Sourcing all changes (events) are stored. The original status ("processing") and the updated status ("shipped") are both preserved as distinct events in the event store.

# Getting Started

## Build and Run the Project with Docker
```
docker-compose up --build
```
This command builds the FastAPI application and runs it alongside a MongoDB instance using Docker.

The FastAPI app will be available at http://localhost:8000.

## Create an Order

Endpoint: POST /orders/
```
curl -X POST "http://localhost:8000/orders/" \
     -H "Content-Type: application/json" \
     -d '{
           "customer_id": "123",
           "product": "Laptop",
           "quantity": 2
         }'
```
Response example:
```
{
  "order_id": "d136ca70-f39c-4232-85c4-e39b3c950226",
  "message": "Order created successfully"
}
```

## Update Order Status

Endpoint: PUT /orders/{order_id}/status/
```
curl -X PUT "http://localhost:8000/orders/{order_id}/status/" \
     -H "Content-Type: application/json" \
     -d '{
           "new_status": "shipped"
         }'
```
Replace {order_id} with the actual order ID from the previous response.

Response example:
```
{
  "order_id": "d136ca70-f39c-4232-85c4-e39b3c950226",
  "message": "Order status updated to shipped"
}
```

## Get Order Details

Endpoint: GET /orders/{order_id}/
```
curl -X GET "http://localhost:8000/orders/{order_id}/"
```
Replace {order_id} with the actual order ID.

Response example:
```
{
  "customer_id": "123",
  "product": "Laptop",
  "quantity": 2,
  "order_id": "d136ca70-f39c-4232-85c4-e39b3c950226",
  "status": "shipped"
}
```
## List All Orders
Endpoint: GET /orders/
```
curl -X GET "http://localhost:8000/orders/"
```
Response example:
```
[
  {
    "customer_id": "123",
    "product": "Laptop",
    "quantity": 2,
    "order_id": "d136ca70-f39c-4232-85c4-e39b3c950226",
    "status": "shipped"
  },
  {
    "customer_id": "123",
    "product": "Laptop",
    "quantity": 2,
    "order_id": "55a6c635-8098-4187-94e6-7e91a43149d6",
    "status": "processing"
  }
]
```

## Delete an Order (Optional - CRUD Operation)

In this implementation, instead of deleting an order, you can mark it as "cancelled" using the update status functionality. Here’s how:

Endpoint: PUT /orders/{order_id}/status/
```
curl -X PUT "http://localhost:8000/orders/{order_id}/status/" \
     -H "Content-Type: application/json" \
     -d '{
           "new_status": "cancelled"
         }'
```
