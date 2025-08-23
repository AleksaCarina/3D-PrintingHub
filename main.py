"""
FastAPI application for the 3D‑PrintingHub project.

This module defines a small FastAPI app that serves a simple landing
page at the root path (`/`). The page is rendered from a Jinja2 template
and includes a short welcome message along with an illustrative image.

To run this app locally, first install the dependencies listed in
`requirements.txt` and then start the server with:

    uvicorn main:app --reload

This will launch a development server on `localhost` port 8000. When
deployed in a production environment, use a proper ASGI server such as
Uvicorn or Hypercorn behind a reverse proxy.
"""

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# Create the FastAPI application instance
app = FastAPI(title="3D Printing Hub", description="A minimal FastAPI setup for serving a landing page.")

# Serve static assets (like images) from the 'static' directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up Jinja2 templating. Template files reside in the 'templates' directory
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request) -> HTMLResponse:
    """Serve the landing page.

    When a user visits the root URL, this endpoint renders the
    ``index.html`` template. The request object is passed into the
    template context as required by FastAPI/Jinja2.

    Args:
        request: The current request instance.

    Returns:
        HTMLResponse: Rendered landing page HTML.
    """
    return templates.TemplateResponse("main.html", {"request": request})
