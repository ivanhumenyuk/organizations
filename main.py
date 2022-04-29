import uvicorn

from orgs.config import dev_config

if __name__ == "__main__":
    uvicorn.run(
        "orgs:create_app",  host=dev_config.get("LOCALHOST"), port=dev_config.get("LOCALHOST_PORT")
    )
