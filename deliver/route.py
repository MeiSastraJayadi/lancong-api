from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from model import route_place_model as route_model
from repository.connection import get_db
from usecase.routes_usecase import create_routes, delete_routes, find_routes_by_id, get_all_routes, update_routes

route_router = APIRouter(
        prefix="/routes", 
        tags=["Route"]
        )

@route_router.get("", response_model=List[route_model.Route], status_code=status.HTTP_200_OK)
def fetch_all_routes(db : Session = Depends(get_db)) : 
    return get_all_routes(db)

@route_router.post("", response_model=route_model.Route, status_code=status.HTTP_201_CREATED)
def create_route(payload : route_model.CreateRoute, db : Session = Depends(get_db)) : 
    data = create_routes(payload, db)
    return data

@route_router.get("/{id}", response_model=route_model.Route, status_code=status.HTTP_200_OK)
def get_route_with_id(id : int, db : Session = Depends(get_db)) : 
    return find_routes_by_id(id, db)

@route_router.delete("/{id}")
def delete_route_with_id(id : int, db : Session = Depends(get_db)) : 
    return delete_routes(id, db)

@route_router.put("/{id}", response_model=route_model.Route, status_code=status.HTTP_200_OK)
def update_route_with_id(id : int, payload : route_model.CreateRoute, db : Session = Depends(get_db)) : 
    return update_routes(payload, id, db)
    
