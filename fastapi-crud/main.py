from fastapi import FastAPI
from database import SessionLocal,engine
from model import Base,Item
from pydantic import BaseModel

app = FastAPI()

Base.metadata.create_all(bind=engine)

class ItemSchema(BaseModel):
    name: str
    price: float
    quantity: int


@app.post("/items/")
def create_items(item: ItemSchema):
    db = SessionLocal()
    db_item = Item(name=item.name, price = item.price, quantity = item.quantity)
    db.add(db_item)
    db.commit()
    db.refresh(db_item) 
    db.close()
    return db_item

@app.get("/items/{item_id}")
def get_items(item_id: int):
    db = SessionLocal()
    db_item = db.query(Item).filter(Item.id == item_id).first()
    db.close()
    if not db_item:
        return {"Error" : {"Item not found"}}
    return db_item

@app.delete("/items/{item_id}")
def delete_item(item_id : int):
    db = SessionLocal()
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if not db_item:
        db.close()
        return {"Error" : "Record Not found"}
    db.delete(db_item)
    db.commit()
    db.close()
    return {"message" : "Item Successfully Deleted"}
    
@app.update("/items/{item_id}")
def update_item(item_id : int, item : ItemSchema):
    db = SessionLocal()
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if not db_item:
        db.close()
        return {"Error" : "Item not found"}
    db_item.name = item.name
    db_item.price = item.price
    db_item.quantity = item.quantity
    db.commit()
    db.refresh(db_item)
    db.close()
    return db_item 