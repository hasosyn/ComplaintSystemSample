from fastapi import FastAPI
from contextlib import asynccontextmanager

from resources.routes import api_router
from db import database


# To solve DeprecationWarning error
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("lifespan start")
    await database.connect()
    yield
    print("lifespan ended")
    await database.disconnect()


app = FastAPI(lifespan=lifespan)

app.include_router(api_router)
