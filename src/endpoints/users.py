from fastapi import APIRouter, Depends, Form, responses, Request, status

from src.model.db import get_db
from ..schemas.users import *
from ..handler.users import *
from init import *

app = APIRouter(prefix="/users", tags=["users"], responses={404: {"msg": "Not Found"}})


@app.post("/register", response_model=BaseUsers)
async def post(
    req: Request,
    item: AddUsers = Depends(BaseUsers.as_form),
    db: Session = Depends(get_db),
):
    user = await HandUser.create_user(db, item)
    if user:
        return responses.RedirectResponse("../", status_code=status.HTTP_302_FOUND)
    return {"msg": "errror"}


@app.post("/login", response_model=BaseUsers)
def login(request: Request, item: AddUsers = Depends(BaseUsers.as_login), db: Session = Depends(get_db)):
    if HandUser.get_username(db, item.username):
        user = HandUser.get_user(db, item)
        if user:
            request.session["username"] = user.username
            return responses.RedirectResponse("../home", status_code=status.HTTP_302_FOUND)
        else:
            return {"msg": "Password is invalid"}
    else:
        return {"msg": "Username Not Found"}


@app.post("/logout")
def logout(req: Request):
    req.session.clear()
    return responses.RedirectResponse("../", status_code=status.HTTP_302_FOUND)
