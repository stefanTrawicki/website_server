from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from .src.drivers import HttpClient

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def home(request: Request):
    context = {
        "request": request,
        "front_page": HttpClient.get("/front-page").get("data"),
        "navigation": HttpClient.get("/navigations").get("data")
    }
    print(context)
    return templates.TemplateResponse("home.html", context)

@app.get("/articles")
async def articles(request: Request):
    data = HttpClient.get(f"/articles")
    print(data)
    context = {
        "request": request,
        "articles": data.get("data")
    }
    return templates.TemplateResponse("articles.html", context)


@app.get("/article/{id}")
async def article(id: int = None):
    return HttpClient.get(f"/articles/{id}")