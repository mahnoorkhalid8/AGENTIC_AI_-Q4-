from fastapi import FastAPI, Path, Query, HTTPException, Body
from pydantic import BaseModel

app = FastAPI()

# pydantic model
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    
# Defining path parameter
@app.get("/items/{item_id}")
async def read_root(
    item_id: int = Path(
        ...,
        title="The ID of the item to get",
        description="A unique identifier for the item",
        ge=1
    )
):
    return {"item_id": item_id}

# Defining query parameter
@app.get("/items/")
async def read_items(
    q: str | None = Query(
        None,
        title="Query string",
        description="Query string for searching items",
        min_length=3,
        max_length=50
    ),
    skip: int = Query(0, ge=0),         # greater than or equal to 0
    limit: int = Query(10, le=100)      # less than or equal to 100
):
    return {"q": q, "skip": skip, "limit": limit}

# Defining path, query and body parameters

@app.put("/items/validate/{item_id}")
async def update_item(
    item_id: int = Path(..., title="Item ID", ge=1),
    q: str | None = Query(None, min_length=3),
    item: Item | None = Body(None, description="OPtional item data (JSON body)")
):
    result: dict[str, int | str | dict] = {"item_id": item_id}
    if q:
        result.update({"q": q})
    if item:
        result.update({"item": item.model_dump()})
    return result