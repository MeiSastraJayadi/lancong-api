from pydantic import BaseModel

from model.database_model import User

class UserRegister(BaseModel) : 
    name : str
    email : str
    password : str
    phone : str
    is_male : bool
    age : int
    card_id : str
    nation : str 

class Login(BaseModel) : 
    email : str
    password : str

class UserDetail(BaseModel) : 
    name : str
    email : str
    phone : str
    is_male : bool
    age : int
    card_id : str
    nation : str 

    class Config:
        orm_mode = True

class Token(BaseModel) : 
    access_token : str
    token_type : str

class TokenData(BaseModel) : 
    email : str | None = None

class UserInDB(UserDetail) : 
    hashed_password : str


