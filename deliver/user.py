from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from repository.connection import get_db
from model.user_model import UserRegister
from usecase.user_usecase import create_user

user_router = APIRouter(
        prefix="/user", 
        tags=["Users"]
        )

@user_router.post("/register")
def register(user : UserRegister, db : Session = Depends(get_db)) : 
    user = create_user(db, user)
    return user

