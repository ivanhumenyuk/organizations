from api import app


@app.get("/")
async def example():
    return {"Hello": "World"}