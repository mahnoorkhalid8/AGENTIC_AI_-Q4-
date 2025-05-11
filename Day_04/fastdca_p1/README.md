# FastAPI Sample Project

This is a basic FastAPI project that demonstrates how to:
- Use path and query parameters
- Validate inputs using Pydantic
- Handle optional request body data

## Requirements

- Python 3.10 or above
- FastAPI
- Uvicorn

## API Endpoints
### 1. GET /items/{item_id}: 
Takes item_id as a path parameter (must be ≥ 1)

### 2. GET /items/: 
Takes optional query parameters:
-q (string, 3-50 characters)
-skip (default: 0)
-limit (default: 10)

### 3. PUT /items/validated/{item_id}:
-Path parameter: item_id
-Query parameter: q (optional)
-JSON body: Optional item data with fields:
*name (string)
*description (optional string)
*price (float)
