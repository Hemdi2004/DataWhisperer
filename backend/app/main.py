from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from app.database.session import engine, Base
from app.api import routes, auth
from app.api.v1.endpoints import chat as chat_router

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="DataWhisperer API")

# Configure CORS
origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include existing API routes
app.include_router(routes.router)
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(chat_router.router, prefix="/api/v1", tags=["Chat"])


@app.get("/")
def read_root():
    return {"message": "Welcome to DataWhisperer API"}