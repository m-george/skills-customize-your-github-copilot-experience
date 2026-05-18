"""
FastAPI REST API Starter Code

This starter file provides the basic structure for building a REST API
with FastAPI. Complete the tasks by implementing the required endpoints
and functionality.
"""

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List

# Initialize the FastAPI application
app = FastAPI(
    title="My REST API",
    description="A simple REST API built with FastAPI",
    version="1.0.0"
)

# TODO: Define a Pydantic model for your items
# Example structure:
# class Item(BaseModel):
#     id: int
#     name: str
#     description: Optional[str] = None
#     price: float


# TODO: Create a data structure to store your items
# You can start with a simple list of dictionaries or use your Pydantic model
items_db = []


# TODO: Task 1 - Create GET endpoints
# - GET /items - return all items
# - GET /items/{item_id} - return a specific item by ID


# TODO: Task 2 - Create POST and PUT endpoints
# - POST /items - add a new item
# - PUT /items/{item_id} - update an existing item


# TODO: Task 3 - Add error handling and validation
# - Return 404 when item not found
# - Return 400 for invalid data
# - Add DELETE endpoint


# TODO: Task 4 (Stretch) - Add query parameters
# - Add skip and limit parameters to GET /items
# - Implement pagination or filtering


# Health check endpoint (example)
@app.get("/")
async def root():
    """
    Health check endpoint.
    """
    return {"message": "API is running!"}


# To run this API locally:
# 1. Install dependencies: pip install fastapi uvicorn
# 2. Run the server: uvicorn app:app --reload
# 3. Visit http://localhost:8000/docs for interactive API documentation
# 4. Test endpoints using the /docs interface or curl/Postman
