from typing import Annotated, List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from model import route_place_model as route_model
from model.user_model import UserDetail
from repository.connection import get_db
from usecase.routes_usecase import create_routes, delete_routes, find_routes_by_id, get_all_routes, update_routes
from usecase.user_usecase import get_current_user

route_router = APIRouter(
        prefix="/routes", 
        tags=["Route"]
        )

@route_router.get("", response_model=List[route_model.Route], status_code=status.HTTP_200_OK)
def fetch_all_routes(current_user : Annotated[UserDetail, Depends(get_current_user)], db : Session = Depends(get_db)) : 
    return get_all_routes(db)

@route_router.post("", response_model=route_model.Route, status_code=status.HTTP_201_CREATED)
def create_route(current_user : Annotated[UserDetail, Depends(get_current_user)], payload : route_model.CreateRoute, db : Session = Depends(get_db)) : 
    if not current_user.is_admin : 
        raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN, 
                detail="User must be an admin"
                )
    data = create_routes(payload, db)
    return data

@route_router.get("/{id}", response_model=route_model.Route, status_code=status.HTTP_200_OK)
def get_route_with_id(current_user : Annotated[UserDetail, Depends(get_current_user)], id : int, db : Session = Depends(get_db)) : 
    return find_routes_by_id(id, db)

@route_router.delete("/{id}")
def delete_route_with_id(current_user : Annotated[UserDetail, Depends(get_current_user)], id : int, db : Session = Depends(get_db)) : 
    if not current_user.is_admin : 
        raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN, 
                detail="User must be an admin"
                )
    return delete_routes(id, db)

@route_router.put("/{id}", response_model=route_model.Route, status_code=status.HTTP_200_OK)
def update_route_with_id(current_user : Annotated[UserDetail, Depends(get_current_user)], id : int, payload : route_model.CreateRoute, db : Session = Depends(get_db)) : 
    if not current_user.is_admin : 
        raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN, 
                detail="User must be an admin"
                )
    return update_routes(payload, id, db)
    
