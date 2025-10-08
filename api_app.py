from fastapi import FastAPI
from domain.item import Item

app = FastAPI()

@app.put("/item")
def add_item(item:Item):
    return "Item Added"

@app.post("/item")
def update_item(item:Item):
    return "Item Updated"

@app.get("/item")
def get_item(item:Item):
    return "Item Retrieved"

@app.delete("/item")
def delete_item(item:Item):
    return "Item Deleted"