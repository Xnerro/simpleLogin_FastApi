from fastapi import Form
from src.handler.users import HandUser
from init import *

app.include_router(route)


@app.get("/home")
async def home(request: Request, db: Session = Depends(get_db)):
    user = HandUser.get_username(db, request.session.get("username"))
    return public.TemplateResponse(
        "templates/home.html",
        {"request": request, "user": user},
    )


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return public.TemplateResponse("index.html", {"request": request})


@app.get("/register", response_class=HTMLResponse)
async def register(req: Request):
    return public.TemplateResponse("templates/register.html", {"request": req})


if __name__ == "__main__":
    uvicorn.run("app:app", reload=True, port=3000)
