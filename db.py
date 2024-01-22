from decouple import config
from databases import Database
from sqlalchemy import MetaData


DATABASE_URL = f"postgresql://{config('DB_USER')}:{config('DB_PASSWORD')}@localhost:5432/complaints"

database = Database(DATABASE_URL)
metadata = MetaData()
