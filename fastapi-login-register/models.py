from sqlalchemy import Table,Column, Integer, String, Float
from db import metadata

users = Table(
    "users",
    metadata,
    Column("id",Integer, primary_key = True),
    Column("username",String(50),nullable = False, unique = False),
    Column("password",String(255))
)