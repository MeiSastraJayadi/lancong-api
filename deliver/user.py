from typing import Annotated
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from repository.connection import get_db
from model.user_model import Token, UserRegister
from usecase.user_usecase import create_user, login_for_token, oauth2_schemes

user_router = APIRouter(
        prefix="/user", 
        tags=["Users"]
        )

@user_router.post("/register")
def register(user : UserRegister, db : Session = Depends(get_db)) : 
    user = create_user(db, user)
    return user

@user_router.post("/login", response_model=Token)
async def login(form_data : Annotated[OAuth2PasswordRequestForm, Depends()], db : Session = Depends(get_db)) : 
    token = login_for_token(form_data, db)
    return token

@user_router.get("/items/")
async def read_items(token: Annotated[str, Depends(oauth2_schemes)]):
    return {"token": token}

    

