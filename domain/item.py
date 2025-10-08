from pydantic import BaseModel, Field

class Item(BaseModel):
    item_id:str
    item_name:str = Field("Sample Item", min_length=3, max_length=50)