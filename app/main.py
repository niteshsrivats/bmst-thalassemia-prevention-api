from contextlib import asynccontextmanager
from typing import Union

from fastapi import FastAPI
from fastapi_versioning import VersionedFastAPI, version
from services import FirebaseService, Neo4JService


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    FirebaseService.init()
    Neo4JService.connect()

    yield
    # Shutdown


app = FastAPI(lifespan=lifespan)


@app.get("/")
@version(1)
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
@version(1)
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


app = VersionedFastAPI(app, version_format="{major}", prefix_format="/v{major}")
