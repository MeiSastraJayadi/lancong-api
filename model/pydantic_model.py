from pydantic import BaseModel

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


