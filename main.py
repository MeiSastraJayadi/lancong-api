from dotenv import load_dotenv
from fastapi import FastAPI
from sqlalchemy.orm import Session

from model import database_model, user_model, place_model, route_model
from repository.connection import engine, SessionLocal

import os

database_model.Base.metadata.create_all(bind=engine)

app = FastAPI()
load_dotenv()

def get_db() : 
    db = SessionLocal()
    try : 
        yield db
    finally : 
        db.close()

@app.get("/")
def hello() : 
    return "Hello World"

url = os.getenv('DATABASE_URL')
print(url)

