from fastapi import FastAPI
import uvicorn
from routers import style

app = FastAPI()

app.include_router(style.router)


if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=6666)