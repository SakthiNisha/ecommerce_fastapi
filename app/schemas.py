from pydantic import BaseModel, EmailStr
from typing import Optional

# Shared fields for User
class UserBase(BaseModel):
    username: str
    email: EmailStr

# Schema for creating a new user
class UserCreate(UserBase):
    password: str  # Password is required during user creation

# Schema for updating an existing user
class UserUpdate(BaseModel):
    username: Optional[str]  # Username is optional for updates
    email: Optional[EmailStr]  # Email is optional for updates
    password: Optional[str]  # Password is optional for updates

# Schema for returning user data in responses
class User(UserBase):
    id: int  # ID is included in responses

    class Config:
        from_attributes = True  # Allow ORM models to be used with this schema
