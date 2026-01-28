from pydantic import BaseModel

class userCreate(BaseModel):
    username: str
    password: str

class userLogin(BaseModel):
    username: str
    password: str