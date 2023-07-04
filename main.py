from dotenv import load_dotenv
from fastapi import FastAPI

from model import database_model
from repository.connection import engine
from deliver.user import user_router
from deliver.place import place_router
from deliver.route import route_router
from deliver.route_place import rp_router

database_model.Base.metadata.create_all(bind=engine)

app = FastAPI()
load_dotenv()

app.include_router(user_router)
app.include_router(place_router)
app.include_router(route_router)
app.include_router(rp_router)



