from fastapi import FastAPI, Request, Depends, middleware
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
import uvicorn
from src.model.db import *
from routes.app import route
from starlette.middleware.sessions import SessionMiddleware

base.metadata.create_all(engine)

public = Jinja2Templates(directory="public")

app = FastAPI(title="Simple Login")
app.mount("/public", StaticFiles(directory="public"), name="static")
app.add_middleware(SessionMiddleware, secret_key="mantap jiwa")


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Process-Time"] = str
    return response
