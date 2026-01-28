from fastapi import FastAPI, HTTPException
from passlib.context import CryptContext
from db import database,engine,metadata
from schema import userCreate,userLogin
from models import users


app = FastAPI()

metadata.create_all(bind = engine)

pwd_context = CryptContext(schemes="bcrypt", deprecated="auto")

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.post("/register")
async def register(user: userCreate):
    query = users.select().where(users.c.username == user.username)
    exisitng_user = await database.fetch_one(query)
    if exisitng_user:
        raise HTTPException(status_code=400, details="Username already exists")
    hashed_password = pwd_context.hash(user.password)
    query = users.insert().values(username = user.username, password = hashed_password)
    await database.execute(query)
    return {"Message" : "User Registered Successfully"}

@app.post("/login")
async def login(user: userLogin):
    query = users.select().where(users.c.username == user.username)
    existing_user = await database.fetch_one(query)
    if not existing_user:
        raise HTTPException(status_code=400, detail="Invalid Username or Password")
    if not pwd_context.verify(user.password, existing_user["password"]):
        raise HTTPException(status_code=400, detail="Invalid Username or Password")
    return {"Message" : "Login Successfullt"}