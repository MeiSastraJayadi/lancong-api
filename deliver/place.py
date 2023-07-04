from typing import Annotated, List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from model import route_place_model as place_model
from model import user_model 
from repository.connection import get_db
from usecase.place_usecase import create_place_usecase, delete_place, get_all_places, get_places_by_id, update_place
from usecase.user_usecase import get_current_user

place_router = APIRouter(
        prefix="/place",
        tags=["Place"]
        )

@place_router.get("", status_code=status.HTTP_200_OK, response_model=List[place_model.Place])
def get_all_place(db : Session = Depends(get_db)):
    return get_all_places(db)

@place_router.get("/{id}", status_code=status.HTTP_200_OK, response_model=place_model.Place)
def get_all_place_with_id(id : int, db : Session = Depends(get_db)) : 
    return get_places_by_id(db, id)


@place_router.post("", status_code=status.HTTP_201_CREATED, response_model=place_model.Place)
def create_place(current_user : Annotated[user_model.UserDetail, Depends(get_current_user)], payload : place_model.CreatePlace, db : Session = Depends(get_db)) : 
    if not current_user.is_admin : 
        raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN, 
                detail="The user is not an admin"
                )
    data = create_place_usecase(db, payload)
    return data

@place_router.delete("/{id}")
def delete_place_with_id(current_user : Annotated[user_model.UserDetail, Depends(get_current_user)], id : int, db : Session = Depends(get_db)) : 
    if not current_user.is_admin : 
        raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN, 
                detail="The user is not an admin"
                )
    return delete_place(db, id)

@place_router.put("/{id}", response_model=place_model.Place, status_code=status.HTTP_200_OK)
def update_place_with_id(current_user : Annotated[user_model.UserDetail, Depends(get_current_user)], id : int, payload : place_model.CreatePlace, db : Session = Depends(get_db)) : 
    if not current_user.is_admin : 
        raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN, 
                detail="The user is not an admin"
                )
    data = update_place(db, id, payload)
    return data
    


