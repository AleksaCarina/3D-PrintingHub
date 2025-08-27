from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from app.db.database import engine, Base
from app.api.routes_auth import router as auth_router

# Initialize FastAPI
app = FastAPI(title="3D Printing Hub", description="API backend for 3D Hub.")

# Allow requests from frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Next.js dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize DB models (for local dev; use Alembic in production)
@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

# Include auth routes (like /login)
app.include_router(auth_router)

# Example: simple health check
@app.get("/health")
async def health_check():
    return JSONResponse({"status": "ok"})

# Optional: keep a test endpoint if needed
@app.get("/")
async def root():
    return JSONResponse({"message": "3D Hub API running"})
