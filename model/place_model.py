from pydantic import BaseModel
from .route_model import Route

class Place(BaseModel) : 
    id : int
    name : str
    city : str
    zip_code : str
    url_coordinate : str


class PlacewithRoute(BaseModel) : 
    id : int
    name : str
    city : str
    zip_code : str
    routes : Route
    routes2 : Route

    class Config:
        orm_mode = True
