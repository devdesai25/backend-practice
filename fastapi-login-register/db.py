from sqlalchemy import create_engine,MetaData
from config import settings
from databases import Database

metadata = MetaData()

database = Database(settings.database_url)
#connecting to the database 
engine = create_engine(
    settings.database_url, 
    echo= True)
