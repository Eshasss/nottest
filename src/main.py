from fastapi import FastAPI
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
#from web.src.database import Database, User

app = FastAPI()

app.mount("/static", StaticFiles(directory="./static", html=True), name="static")
@app.get("/")
async def home():
    return FileResponse("static/html/index.html")

@app.get("/end/")
async def hello():
    return FileResponse("static/html/end.html")
