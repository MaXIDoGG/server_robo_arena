from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


def hex_to_rgb(color_hex):
    hex = color_hex.lstrip("#")
    return tuple(int(hex[i : i + 2], 16) for i in (0, 2, 4))


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/color", response_class=HTMLResponse)
async def color(request: Request):
    return templates.TemplateResponse("color.html", {"request": request})


@app.post("/change_color")
async def change_color(request: Request, color=Form()):
    print(hex_to_rgb(color))


@app.get("/voting", response_class=HTMLResponse)
async def voting(request: Request):
    return templates.TemplateResponse("voting.html", {"request": request})


@app.post("/vote", response_class=HTMLResponse)
async def vote():
    pass
