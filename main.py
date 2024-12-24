import asyncio

from fastapi import (FastAPI,
                     BackgroundTasks,
                     Request)
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse


app = FastAPI()
templates = Jinja2Templates("templates")


@app.get("/", response_class = HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(request=request, name = "index.html")


async def simulation():
    await asyncio.sleep(10)
    print("aboba")



@app.get("/json-response")
async def json_response(background_tasks: BackgroundTasks):
    background_tasks.add_task(simulation)
    print("done")
    return {"All" : "Set"}
