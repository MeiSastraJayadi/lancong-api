from fastapi import HTTPException, Response, status
from sqlalchemy.orm import Session
from model.database_model import Route
from model.route_place_model import CreateRoute
from usecase.place_usecase import find_place

def get_all_routes(db : Session) : 
    return db.query(Route).all()

def find_routes(id : int, db : Session) : 
    routes = db.query(Route).filter(Route.id == id)
    if not routes.first() : 
        raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail=f"Place with id {id} not found"
                )
    return routes

def find_routes_by_id(id : int, db : Session) : 
    return find_routes(id, db).first()

def delete_routes(id : int, db : Session) : 
    routes = find_routes(id, db)
    routes.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

def create_routes(route : CreateRoute, db : Session) : 
    route_db = Route(
            price = route.price,
            duration = route.duration, 
            start = str(route.start).split("+")[0]
            )
    db.add(route_db)
    db.commit()
    db.refresh(route_db)
    return route_db

def update_routes(payload : CreateRoute, id : int, db : Session) : 
    route = find_routes(id, db)
    data = payload.dict(exclude_unset=True)
    print(data)
    route.update(data, synchronize_session=False)
    print(data)
    db.commit()
    db.refresh(route.first())
    return route.first()

