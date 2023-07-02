from dotenv import load_dotenv
from fastapi import FastAPI
from sqlalchemy.orm import Session

from model import database_model, user_model, route_place_model
from repository.connection import engine, SessionLocal
from deliver.user import user_router


database_model.Base.metadata.create_all(bind=engine)

app = FastAPI()
load_dotenv()


# app.add_route("/", user_router)

@app.get("/")
def hello() : 
    return "Hello World"
