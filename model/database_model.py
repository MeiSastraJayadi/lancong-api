from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, column
from sqlalchemy.orm import relationship
from repository.connection import Base 

class User(Base) : 
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(90))
    email = Column(String(60), unique=True)
    hashed_password = Column(String(300))
    phone = Column(String(20))
    is_male = Column(Boolean, default=False)
    age = Column(Integer)
    card_id = Column(String(30))
    nation = Column(String(30))

    books = relationship("Book", back_populates="users")

class Place(Base) : 
    __tablename__ = "places"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(30))
    city = Column(String(30))
    zip_code = Column(String(50))
    url_coordinate = Column(String(400))
    
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

class Payment(Base) : 
    __tablename__ = "payments"
    id = Column(Integer, primary_key=True, index=True)
    total = Column(Integer)
    payment_date = Column(DateTime)

    books = relationship("Book", back_populates="payments")

class Book(Base) : 
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    route_id = Column(Integer, ForeignKey("routes.id"))
    payment_id = Column(Integer, ForeignKey("payments.id"))

    users = relationship("User", back_populates="books")
    routes = relationship("Route", back_populates="books")
    payments = relationship("Payment", back_populates="books")



