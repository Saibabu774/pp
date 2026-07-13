from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers.job import router as job_router
from .routers.auth import router as auth_router  # <-- ADDED

app = FastAPI(
    title="Async Job Processing System",
    version="1.0.0",
    description="Backend API for Async Job Queue"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # better than "*" when using credentials
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Routers
app.include_router(
    auth_router,  # <-- ADDED
    prefix="/auth",
    tags=["Auth"]
)

app.include_router(
    job_router,
    prefix="/jobs",
    tags=["Jobs"]
)

@app.get("/")
def root():
    return {
        "message": "Async Job Processing API Running",
        "status": "success"
    }

@app.get("/health")
def health():
    return {
        "server": "Running",
        "queue": "Ready",
        "worker": "Ready"
    }