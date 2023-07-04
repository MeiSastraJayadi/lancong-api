from pydantic import BaseModel

class Place(BaseModel) : 
    id : int
    name : str
    city : str
    zip_code : str
    url_coordinate : str

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
    place1 : Place 
    place2 : Place
    price : int
    duration : int

    class Config : 
        orm_mode=True

class CreateRoute(BaseModel) : 
    place1_id : int 
    place2_id : int 
    price : int
    duration : int

    class Config : 
        orm_mode = True


class PlacewithRoute(BaseModel) : 
    id : int
    name : str
    city : str
    zip_code : str
    routes : Route
    routes2 : Route

    class Config:
        orm_mode = True


class RoutePlace(BaseModel) : 
    id : int
    place2 : Place
    place2 : Place
    price : int
    duration : int
    
    class Config:
        orm_mode = True

