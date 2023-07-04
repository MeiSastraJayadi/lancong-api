from enum import IntEnum
from operator import index
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime 
from sqlalchemy.orm import relationship
from repository.connection import Base 

class User(Base) : 
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(90))
    username = Column(String(20), unique=True)
    email = Column(String(60), unique=True)
    hashed_password = Column(String(300))
    phone = Column(String(20))
    is_male = Column(Boolean, default=False)
    age = Column(Integer)
    card_id = Column(String(30))
    nation = Column(String(30))
    is_admin = Column(Boolean, default=False)

    books = relationship("Book", back_populates="users")

class Place(Base) : 
    __tablename__ = "places"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(30))
    city = Column(String(30))
    zip_code = Column(String(50))
    url_coordinate = Column(String(400))

    routes = relationship("Route", secondary="route_places", back_populates="places")


class Route(Base) : 
    __tablename__ = "routes"
    id = Column(Integer, primary_key=True, index=True)
    price = Column(Integer)
    duration = Column(Integer)

    places = relationship("Place", secondary="route_places", back_populates="routes")

    books = relationship("Book", back_populates="routes")


class RoutePlace(Base) : 
    __tablename__ = "route_places"
    id = Column(Integer, primary_key=True, index=True)
    route_id = Column(Integer, ForeignKey("routes.id"))
    place_id = Column(Integer, ForeignKey("places.id"))

class Book(Base) : 
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    route_id = Column(Integer, ForeignKey("routes.id"))
    date = Column(DateTime)  

    users = relationship("User", back_populates="books")
    routes = relationship("Route", back_populates="books")




