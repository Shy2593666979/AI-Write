import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from backend.routers import style, tool

app = FastAPI()

app.include_router(style.router, prefix="/tool")
app.include_router(tool.router)

app.mount("/upimg", StaticFiles(directory="upimg"), name="upimg")

if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=6666)