
from .db_manager import user_exist, add_user, login_check, change_password
import json
from fastapi import FastAPI,Request
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles


app = FastAPI()
app.mount("/static", StaticFiles(directory="./static", html=True), name="static")

@app.get("/")
async def home():
    return FileResponse("static/html/index.html")

@app.post("/newguy/")
async def home(data: Request):
    data = await data.json()
    if user_exist(data):
        return JSONResponse(content={}, status_code=403)
    else:
        add_user(data)
        return JSONResponse(content={}, status_code=200)

@app.post("/oldguy/")
async def find(data: Request):
    data = await data.json()
    if login_check(data):
        return JSONResponse(content={}, status_code=200)
    else:
        #неверный пароль или невырный токен или неверный ник
        return JSONResponse(content={}, status_code=404)

@app.get("/end/")
async def hello():
    return FileResponse("static/html/end.html")


@app.get("/login/")
async def login():
    return FileResponse("static/html/login.html")

@app.get("/register/")
async def register():
    return FileResponse("static/html/register.html")