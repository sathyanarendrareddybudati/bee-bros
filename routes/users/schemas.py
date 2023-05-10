from pydantic import BaseModel, EmailStr, constr
from typing import Optional

class UsersIN(BaseModel):
    email : EmailStr
    full_name : str
    password : str
    phone_number : constr(regex=r'^\+?[1-9]\d{1,14}$')

class UsersOUT(BaseModel):
    email :EmailStr
    full_name : str
    phone_number :str

    class Config:
        orm_mode = True

class LoginIN(BaseModel):
    email : EmailStr
    full_name : str
    password : str

class Token(BaseModel):
    access_token : str
    token_type : str
    message : str

class TokenData(BaseModel):
    id : Optional[str] = None