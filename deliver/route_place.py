
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from model import route_place_model, user_model
from repository.connection import get_db
from usecase.route_place_usecase import create_route_place, delete_route_place
from usecase.user_usecase import get_current_user


rp_router = APIRouter(
        prefix="/route-place",
        tags=["Route Place"]
        )

@rp_router.post("", status_code=status.HTTP_201_CREATED, response_model=route_place_model.RoutePlace)
def create_route_with_place(current_user : Annotated[user_model.UserDetail, Depends(get_current_user)], payload : route_place_model.RoutePlace, db : Session = Depends(get_db)) : 
    if not current_user.is_admin : 
        raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Just an admin can create this relation"
                )
    return create_route_place(db, payload)

@rp_router.delete("") 
def delete_route_with_place(current_user : Annotated[user_model.UserDetail, Depends(get_current_user)], payload : route_place_model.RoutePlace, db : Session = Depends(get_db)) : 
    if not current_user.is_admin : 
        raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Just an admin can create this relation"
                )
    return delete_route_place(db, payload)


