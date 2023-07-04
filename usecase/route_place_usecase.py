from fastapi import HTTPException, Response, status
from sqlalchemy.orm import Session
from model import database_model, route_place_model


def create_route_place(db : Session, payload : route_place_model.RoutePlace) : 
    place_db = database_model.RoutePlace(
            route_id = payload.route_id, 
            place_id = payload.place_id
            )
    db.add(place_db)
    db.commit()
    db.refresh(place_db)
    return place_db

def delete_route_place(db : Session, payload : route_place_model.RoutePlace) : 
    route = db.query(database_model.RoutePlace).filter(
            database_model.RoutePlace.route_id == payload.route_id, database_model.RoutePlace.place_id == payload.place_id)

    if not route : 
        raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Relation not found"
                )
    route.delete(synchronize_session=False)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


