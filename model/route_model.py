from pydantic import BaseModel
from .place_model import Place

class Route(BaseModel) : 
    id : int
    place1 : Place 
    place2 : Place
    price : int
    duration : int

class RoutePlace(BaseModel) : 
    id : int
    place2 : Place
    place2 : Place
    price : int
    duration : int
    
    class Config:
        orm_mode = True

