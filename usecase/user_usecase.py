from datetime import datetime, timedelta
from typing import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from model.database_model import User
from model.user_model import TokenData, UserRegister

from passlib.context import CryptContext
from jose import JWTError, jwt

import os


SECRET_KEY = str(os.getenv("SECRET_KEY"))
ALGORITHM = "HS256"
EXP = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto") 
oauth2_schemes = OAuth2PasswordBearer(tokenUrl="/user/login")

def verify_password(hashed_password:str, plain_password:str) -> bool : 
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hashed(password:str) -> str :
    return pwd_context.hash(password)

def get_user(db, username:str) : 
    return db.query(User).filter(User.username == username).first()

def create_access_token(data : dict, expires_delta : timedelta | None = None) : 
    to_encode = data.copy()
    if expires_delta : 
        expire = datetime.utcnow() + expires_delta
    else : 
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp" : expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token : Annotated[str, Depends(oauth2_schemes)], db : Session) : 
    credential_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Could not validated credential",
            headers={"WWW-Authenticate":"Bearer"}
            )
    try : 
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        username = payload.get("sub")
        if username is None : 
            raise credential_exception
        token_data = TokenData(username=username)
    except JWTError : 
        raise credential_exception
    user = get_user(db, username)
    if user is None : 
        raise credential_exception
    return user

def create_user(db : Session, user : UserRegister) : 
    hashed_password = get_password_hashed(user.password)
    user.password = hashed_password
    user_db = User(
            name = user.name, 
            username = user.username,
            email = user.email,
            hashed_password = user.password,
            phone = user.phone, 
            is_male = user.is_male,
            age = user.age, 
            card_id = user.card_id, 
            nation = user.nation
            )

    db.add(user_db)
    db.commit()
    db.refresh(user_db)
    return user_db 

def authenticate_user(username: str, password : str, db : Session) : 
    user = get_user(db, username)
    if not user : 
        return False
    if not verify_password(str(user.hashed_password), password) : 
        return False
    return user

def login_for_token(form_data : Annotated[OAuth2PasswordRequestForm, Depends()], db : Session) : 
    user = authenticate_user(form_data.username, form_data.password, db) 
    if not user : 
        raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password", 
                headers={"WWW-Authenticate":"Bearer"}
                )
    access_token_expire = timedelta(minutes=EXP)
    access_token = create_access_token(data={"sub" : user.username}, expires_delta=access_token_expire)
    return {"access_token" : access_token, "token_type" : "bearer"}


