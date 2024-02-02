
from .db_manager import user_exist, add_user, login_check, change_password

from fastapi import FastAPI
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles


app = FastAPI()
app.mount("/static", StaticFiles(directory="./static", html=True), name="static")

@app.get("/")
async def home():
    return FileResponse("static/html/index.html")



@app.get("/end/")
async def hello():
    return FileResponse("static/html/end.html")