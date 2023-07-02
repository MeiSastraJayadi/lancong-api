from typing import Annotated
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from repository.connection import get_db
from model.user_model import UserRegister
from usecase.user_usecase import create_user, login_for_token

user_router = APIRouter(
        prefix="/user", 
        tags=["Users"]
        )

@user_router.post("/register")
def register(user : UserRegister, db : Session = Depends(get_db)) : 
    user = create_user(db, user)
    return user

@user_router.post("/login")
async def login(form_data : Annotated[OAuth2PasswordRequestForm, Depends()], db : Session = Depends(get_db)) : 
    token = login_for_token(form_data, db)
    return token
    

