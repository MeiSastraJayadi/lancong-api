from datetime import datetime
from pydantic import BaseModel

class CreateBook(BaseModel) :
    route_id : int

    class Config : 
        orm_mode = True

class Book(BaseModel) :
    id : int
    user_id : int
    route_id : int

    class Config : 
        orm_mode = True


    
