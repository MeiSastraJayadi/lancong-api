from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from model.database_model import Place
from repository.connection import get_db
from usecase.place_usecase import get_all_places

place_router = APIRouter(
        prefix="/place",
        tags=["Place"]
        )

@place_router.get("/", status_code=status.HTTP_200_OK, response_model=List[Place])
def get_all_place(db : Session = Depends(get_db)):
    return get_all_places(db)


