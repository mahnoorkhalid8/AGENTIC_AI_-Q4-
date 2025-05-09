from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello World from Mahnoor Khalid :)"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return{"item id": {item_id}, "q": q}
