from datetime import date, datetime
from pydantic import BaseModel

class CreateBook(BaseModel) :
    route_id : int
    start_date : date

    class Config : 
        orm_mode = True

class Book(BaseModel) :
    id : int
    user_id : int
    route_id : int
    start_date : date
    date : datetime

    class Config : 
        orm_mode = True


    
