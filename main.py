from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#input parameters
class Item(BaseModel):
    name: str
    phone: int
    age: int
    password: str="Dont show this my man"
#response class where only certain fields are sent
class ItemResponse(BaseModel):
    name: str
    phone: int
    age: int

@app.post("/items/",response_model=ItemResponse)
def create_item(item:Item):
    return item
#@app.get("/items/{item_id}")
#def demo(item_id: str,q : str = None):
#    return {"item": item_id,"query" : q}