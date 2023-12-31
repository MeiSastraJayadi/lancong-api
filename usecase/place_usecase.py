from fastapi import HTTPException, Response, status
from sqlalchemy.orm import Session

from model.database_model import Place
from model.route_place_model import CreatePlace as Pc  

def create_place_usecase(db : Session, place : Pc) : 
    place_db = Place(
            name = place.name,
            city = place.city, 
            zip_code = place.zip_code,
            url_coordinate = place.url_coordinate
            )
    db.add(place_db)
    db.commit()
    db.refresh(place_db)
    return place_db

def get_all_places(db : Session) : 
    return db.query(Place).all()

def get_places_by_id(db : Session, id : int) : 
    place = db.query(Place).filter(Place.id == id).first()
    if not place : 
        raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Place with id {id} not found"
                )
    return place

def find_place(db : Session, id : int) : 
    place = db.query(Place).filter(Place.id == id)
    place_first = place.first()
    if not place_first : 
        raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Place with id {id} not found"
                )
    return place


def delete_place(db : Session, id : int) : 
    place = find_place(db, id)
    place.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

def update_place(db : Session, id : int, payload : Pc) : 
    place = find_place(db, id)
    data = payload.dict(exclude_unset=True)
    place.update(data, synchronize_session=False)
    db.commit()
    db.refresh(place.first())
    return place.first()
    
    

