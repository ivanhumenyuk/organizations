from fastapi import FastAPI
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from api.config import dev_config

# DATABASE_URL = f"postgresql+asyncpg://{dev_config.get('POSTGRES_USER')}:" \
#                f"{dev_config.get('POSTGRES_PW')}" \
#                f"@{dev_config.get('POSTGRES_URL')}/" \
#                f"{dev_config.get('POSTGRES_DB')}"

DATABASE_URL = f"postgresql+asyncpg://{dev_config.get('POSTGRES_USER')}:" \
               f"{dev_config.get('POSTGRES_PW')}" \
               f"@{dev_config.get('POSTGRES_URL')}/" \
               f"{dev_config.get('POSTGRES_DB')}"

app = FastAPI()

engine = create_async_engine(DATABASE_URL, future=True, echo=True)
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
Base = declarative_base(bind=engine)


@app.on_event("startup")
async def startup():
    # create db tables
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


def create_app() -> FastAPI:
    from api import routers

    for router in routers:
        app.include_router(router)

    return app
