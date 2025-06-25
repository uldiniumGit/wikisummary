from fastapi import FastAPI
from app.api.endpoints import router
from app.core.container import Container
from app.db.models import Base

app = FastAPI()
container = Container()
container.init_resources()
container.wire(modules=["app.api.endpoints"])
app.container = container
app.include_router(router, prefix="/api")


@app.on_event("startup")
async def startup():
    engine = container.engine()
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
