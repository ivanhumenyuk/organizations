from fastapi import FastAPI
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker

app = FastAPI()


@app.on_event("startup")
async def startup():
    from db_engine import engine, Base
    # create db tables
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


def create_app() -> FastAPI:
    from api import routers

    for router in routers:
        app.include_router(router)

    return app
