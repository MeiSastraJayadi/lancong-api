from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from model import route_place_model as place_model
from repository.connection import get_db
from usecase.place_usecase import create_place_usecase, delete_place, get_all_places, update_place

place_router = APIRouter(
        prefix="/place",
        tags=["Place"]
        )

@place_router.get("", status_code=status.HTTP_200_OK, response_model=List[place_model.Place])
def get_all_place(db : Session = Depends(get_db)):
    return get_all_places(db)

@place_router.post("", status_code=status.HTTP_201_CREATED, response_model=place_model.Place)
def create_place(payload : place_model.CreatePlace, db : Session = Depends(get_db)) : 
    data = create_place_usecase(db, payload)
    return data

@place_router.delete("/{id}")
def delete_place_with_id(id : int, db : Session = Depends(get_db)) : 
    return delete_place(db, id)

@place_router.put("/{id}", response_model=place_model.Place, status_code=status.HTTP_200_OK)
def update_place_with_id(id : int, payload : place_model.CreatePlace, db : Session = Depends(get_db)) : 
    data = update_place(db, id, payload)
    return data
    


