from typing import Annotated
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from model import books_model, user_model
from repository.connection import get_db
from usecase.book_usecase import create_book, get_book
from usecase.user_usecase import get_current_user

book_route = APIRouter(
        prefix="/books",
        tags=["Book"]
        )

@book_route.get("", response_model=books_model.Book, status_code=status.HTTP_200_OK)
def get_all_book(current_user : Annotated[user_model.UserDetail, Depends(get_current_user)], db : Session = Depends(get_db)) : 
    return get_book(current_user.id, db)

@book_route.post("", response_model=books_model.Book, status_code=status.HTTP_201_CREATED)
def create_books(current_user : Annotated[user_model.UserDetail, Depends(get_current_user)], payload : books_model.CreateBook, db : Session = Depends(get_db)) : 
    return create_book(payload, db, current_user.id)

