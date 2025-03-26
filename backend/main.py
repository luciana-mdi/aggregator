from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import project_routes
import uvicorn

app = FastAPI(
    title="Aggregator API",
    description="Backend for Mormedi's Aggregator tool",
    version="0.1.0",
)

# CORS setup (adjust if you have a specific frontend origin)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # replace with your frontend URL in prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include project-related routes
app.include_router(project_routes.router, prefix="/api/projects", tags=["Projects"])

# Optional entry point for local dev
if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
