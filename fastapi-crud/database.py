from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from config import settings

#creating a base class which stores all the database 
Base = declarative_base()
#engine to connect and work with database
engine = create_engine(
    settings.database_url,
    pool_pre_ping=True
)

#a object to create sessions for each database session (add,update,delete,etc.)
SessionLocal = sessionmaker(
    bind = engine, 
    autoflush=False,
    autocommit=False
)