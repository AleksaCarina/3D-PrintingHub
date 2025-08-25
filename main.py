
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

# Create the FastAPI application instance
app = FastAPI(title="3D Printing Hub", description="A minimal FastAPI setup for serving a landing page.")

# Serve static assets (like images) from the 'static' directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up Jinja2 templating. Template files reside in the 'templates' directory
templates = Jinja2Templates(directory="templates")


@app.get("/", name="main", response_class=HTMLResponse)
async def read_root(request: Request) -> HTMLResponse:
    
    return templates.TemplateResponse("main.html", {"request": request})

@app.get("/login", response_class=HTMLResponse)
async def read_root(request: Request) -> HTMLResponse:

    return templates.TemplateResponse("login.html", {"request": request})   


@app.post("/login")
async def login_post(request: Request):
    data = await request.json()
    username = data.get("username")
    password = data.get("password")

    # Primer validacije
    if username == "admin" and password == "1234":
        return JSONResponse({"success": True})
    return JSONResponse({"success": False, "message": "Invalid credentials"})


@app.get("/home", name="home", response_class=HTMLResponse)
async def home_page(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})