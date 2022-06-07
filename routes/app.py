from fastapi import APIRouter
from src.endpoints.users import app

route = APIRouter()

route.include_router(app)
