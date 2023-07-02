from pydantic import BaseModel

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
