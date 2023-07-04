from typing import List
from pydantic import BaseModel

class PlaceRelation(BaseModel) : 
    id : int
    name : str
    city : str
    zip_code : str
    url_coordinate : str

    class Config: 
        orm_mode = True

class RouteRelation(BaseModel) : 
    id : int
    price : int
    duration : int

    class Config : 
        orm_mode=True


class Place(BaseModel) : 
    id : int
    name : str
    city : str
    zip_code : str
    url_coordinate : str
    routes : List[RouteRelation]

    class Config: 
        orm_mode = True

class CreatePlace(BaseModel) : 
    name : str
    city : str
    zip_code : str
    url_coordinate : str

    class Config:
        orm_mode = True

class Route(BaseModel) : 
    id : int
    price : int
    duration : int
    places : List[PlaceRelation]

    class Config : 
        orm_mode=True

class CreateRoute(BaseModel) : 
    price : int
    duration : int

    class Config : 
        orm_mode = True


class RoutePlace(BaseModel) : 
    id : int
    route_id : int
    place_id : int
    
    class Config:
        orm_mode = True

