# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn to build a complete REST API using the FastAPI framework. You'll create endpoints that handle HTTP requests, manage data, validate inputs, and return structured responses—all with automatic interactive documentation.

## 📝 Tasks

### 🛠️ Create a Basic API with GET Endpoints

#### Description
Build the foundation of a REST API that serves data about a collection of items (books, products, or tasks). Create endpoints to retrieve all items and fetch a specific item by ID.

#### Requirements
Completed program should:

- Import FastAPI and create an application instance
- Define a data structure (list of dictionaries or Pydantic models) for items
- Create a GET endpoint `/items` that returns all items
- Create a GET endpoint `/items/{item_id}` that returns a specific item by ID
- Run the application with `uvicorn` and verify endpoints work in your browser or with a tool like curl or Postman

### 🛠️ Add POST and PUT Endpoints for Data Manipulation

#### Description
Extend your API with endpoints that allow clients to create new items and update existing ones. Implement proper request handling and response codes.

#### Requirements
Completed program should:

- Create a POST endpoint `/items` that accepts JSON data and adds a new item to the collection
- Create a PUT endpoint `/items/{item_id}` that updates an existing item
- Return appropriate HTTP status codes (201 for creation, 200 for successful updates)
- Return the created or updated item in the response
- Test all endpoints to ensure data is properly stored and retrieved

### 🛠️ Implement Request Validation and Error Handling

#### Description
Make your API robust by validating incoming data and handling errors gracefully. Use Pydantic models to ensure data quality and return meaningful error messages.

#### Requirements
Completed program should:

- Define a Pydantic model with required fields and type hints (e.g., `Item` with `id`, `name`, `description`, `price`)
- Validate all incoming request data against the model
- Return a 404 error with a descriptive message when requesting a non-existent item
- Return a 400 error with validation details when request data is invalid
- Include a DELETE endpoint `/items/{item_id}` that removes an item and returns appropriate status codes

### 🛠️ Stretch Goal: Add Query Parameters and Documentation

#### Description
Enhance your API with filtering and search capabilities, and leverage FastAPI's automatic API documentation features.

#### Requirements
Completed program should:

- Add query parameters to the GET `/items` endpoint (e.g., `skip`, `limit` for pagination, or `search` for filtering by name)
- Test query parameters with various values
- Visit the automatically generated API documentation at `/docs` (Swagger UI)
- Verify that all your endpoints are documented with proper descriptions
- Add docstrings and query parameter descriptions to your endpoint functions
