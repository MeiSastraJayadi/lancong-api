from datetime import datetime
from sqlalchemy.orm import Session

from model import database_model
from model.books_model import CreateBook


def get_book(id : int, db : Session) : 
    book = db.query(database_model.Book).filter(database_model.Book.user_id == id) 
    return book

def create_book(payload : CreateBook, db : Session, id : int) : 
    tm = str(datetime.now())
    book = database_model.Book(
                user_id = id,
                route_id = payload.route_id,
                date = tm
            )

    db.add(book)
    db.commit()
    db.refresh(book)
    return book
    

