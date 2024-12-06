from sqlalchemy import Column, Integer, String
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)  # Specify length for String
    email = Column(String(100), unique=True, index=True)    # Specify length for String
    hashed_password = Column(String(255))                   # Specify length for String

