from fastapi import FastAPI
from contextlib import asynccontextmanager
from starlette.middleware.cors import CORSMiddleware

from resources.routes import api_router
from db import database

origins = [
    "http://localhost",
    "http://localhost:4200",
]


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
app.add_middleware(CORSMiddleware, allow_origins=origins,
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"])
