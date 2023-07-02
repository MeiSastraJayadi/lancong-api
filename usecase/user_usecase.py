from datetime import datetime, timedelta
from typing import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from model.database_model import User
from model.user_model import TokenData, UserRegister, UserInDB

from passlib.context import CryptContext
from jose import JWTError, jwt

import os


SECRET_KEY = str(os.getenv("SECRET_KEY"))
ALGORITHM = "HS256"
EXP = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto") 
oauth2_schemes = OAuth2PasswordBearer(tokenUrl="login")

def verify_password(hashed_password:str, plain_password:str) -> bool : 
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hashed(password:str) -> str :
    return pwd_context.hash(password)

def get_user(db, email:str) : 
    if email in db : 
        user_dict = db[email]
        return UserInDB(**user_dict)

def create_access_token(data : dict, expires_delta : timedelta | None = None) : 
    to_encode = data.copy()
    if expires_delta : 
        expire = datetime.utcnow() + expires_delta
    else : 
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp" : expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token : Annotated[str, Depends(oauth2_schemes)]) : 
    credential_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Could not validated credential",
            headers={"WWW-Authenticate":"Bearer"}
            )
    try : 
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        email  = payload.get("sub")
        if email is None : 
            raise credential_exception
        token_data = TokenData(email=email)
    except JWTError : 
        raise credential_exception

def create_user(db : Session, user : UserRegister) : 
    hashed_password = get_password_hashed(user.password)
    user.password = hashed_password
    user_db = User(
            name = user.name, 
            email = user.email,
            hashed_password = user.password,
            phone = user.phone, 
            is_male = user.is_male,
            age = user.age, 
            card_id = user.card_id, 
            nation = user.nation
            )

    print(user_db)
    db.add(user_db)
    db.commit()
    db.refresh(user_db)
    return user_db 


