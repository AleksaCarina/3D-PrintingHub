from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.db.database import engine, Base
from app.api.routes_auth import router as auth_router

# Paths relative to this file (app/)
BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = BASE_DIR / "static"
TEMPLATES_DIR = BASE_DIR / "templates"

def init_models():
    # Create tables if they don't exist (good for local dev; use Alembic in prod)
    Base.metadata.create_all(bind=engine)

# FastAPI app
app = FastAPI(title="3D Printing Hub", description="A minimal FastAPI setup for serving a landing page.")

# Startup: init DB schema
@app.on_event("startup")
def on_startup():
    init_models()

# Static files (only mount if the directory exists)
if STATIC_DIR.is_dir():
    app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")

# Templates (optional; fallback HTML if not present)
templates = Jinja2Templates(directory=str(TEMPLATES_DIR)) if TEMPLATES_DIR.is_dir() else None

# Auth routes
app.include_router(auth_router)

# Routes
@app.get("/", response_class=HTMLResponse)
async def home(request: Request) -> HTMLResponse:
    if templates:
        return templates.TemplateResponse("main.html", {"request": request})
    return HTMLResponse("<h1>3D Printing Hub</h1><p>Templates folder not found.</p>")

@app.get("/login", response_class=HTMLResponse)
async def login_page(request: Request) -> HTMLResponse:
    if templates:
        return templates.TemplateResponse("login.html", {"request": request})
    return HTMLResponse("<h1>Login</h1><p>Templates folder not found.</p>")
