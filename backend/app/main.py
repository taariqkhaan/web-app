# FastAPI entry point

from fastapi import FastAPI
from app.database import engine, Base

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "Project Management API is running"}

