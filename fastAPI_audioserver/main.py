import uvicorn
from fastapi import FastAPI
from starlette.requests import Request
from starlette.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles



app = FastAPI(title="AudioServer")
app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")

@app.get("/")
def main_page(request: Request):
    return templates.TemplateResponse("audio_main_page.html", {"request": request})



uvicorn.run(app, port=8004)