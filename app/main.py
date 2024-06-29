from fastapi import FastAPI
import uvicorn
from routers import style

app = FastAPI()

app.include_router(style.router, prefix="/api")


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port="6666")