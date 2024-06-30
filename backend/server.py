from fastapi import FastAPI
import uvicorn
from routers import style, tool

app = FastAPI()

app.include_router(style.router, prefix="/tool")
app.include_router(tool.router)


if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=6666)