from fastapi import FastAPI
from controller.address_book_api import router as address_book_router
# from domain.item import Item

app = FastAPI()
api_app = FastAPI()

api_app.include_router(address_book_router)
# api_app.include_router(ot)her_api_router)

app.mount("/api/v1", api_app)

# @app.put("/item")
# def add_item(item:Item):
#     return "Item Added"

# @app.post("/item")
# def update_item(item:Item):
#     return "Item Updated"

# @app.get("/item")
# def get_item(item:Item):
#     return "Item Retrieved"

# @app.delete("/item")
# def delete_item(item:Item):
#     return "Item Deleted"