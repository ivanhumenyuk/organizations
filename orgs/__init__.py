from fastapi import FastAPI

from orgs.db_engine import Base, engine

app = FastAPI()

# use without alembic
# @app.on_event("startup")
# async def startup():
#     """Creating database """
#     # create db tables
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.drop_all)
#         await conn.run_sync(Base.metadata.create_all)


def create_app() -> FastAPI:
    from orgs.api import routers

    for router in routers:
        app.include_router(router)

    from fastapi_pagination import add_pagination

    # adding pagination
    add_pagination(app)

    return app
