import uvicorn
from api.config import dev_config


if __name__ == "__main__":
    uvicorn.run(
        "api:app",  host=dev_config.get("LOCALHOST"), port=dev_config.get("LOCALHOST_PORT")
    )
