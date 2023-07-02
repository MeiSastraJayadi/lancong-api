from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from ..repository.connection import Base 

class User(Base) : 
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True)
    hashed_password = Column(String)
    phone = Column(String)
    is_male = Column(Boolean, default=False)
    age = Column(Integer)
    card_id = Column(String)
    nation = Column(String)

    books = relationship("Book", back_populates="users")
    payments = relationship("Payment", back_populates="users")

class Place(Base) : 
    __tablename__ = "places"
    id = Column(Integer, primary_key=True, index=True)
    city = Column(String)
    zip_code = Column(String)
    url_coordinate = Column(String)
    
    routes = relationship("Route", back_populates="place1")
    routes2 = relationship("Route", back_populates="place2")

class Route(Base) : 
    __tablename__ = "routes"
    id = Column(Integer, primary_key=True, index=True)
    place1_id = Column(Integer, ForeignKey("places.id"))
    place2_id = Column(Integer, ForeignKey("places.id"))
    price = Column(Integer)
    duration = Column(Integer)

    books = relationship("Book", back_populates="routes")
    place1 = relationship("Place", back_populates="routes")
    place2 = relationship("Place", back_populates="routes2")


class Book(Base) : 
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    route_id = Column(Integer, ForeignKey("routes.id"))
    book_date = Column(DateTime)

    users = relationship("User", back_populates="books")
    routes = relationship("Route", back_populates="books")

class Payment(Base) : 
    __tablename__ = "payments"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    book_date = Column(DateTime)

    users = relationship("User", back_populates="payments")


