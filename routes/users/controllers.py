from database import get_database_session
from fastapi import APIRouter,HTTPException,status,Depends
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from .models import Users
from .schemas import UsersIN,UsersOUT,Token
from .helpers import hash,verify,create_access_token

router = APIRouter(
    tags=['USERS'],
)

@router.get("/users/{user_id}",status_code=status.HTTP_200_OK,response_model=UsersOUT)
def get_users(users_id:int, db:Session=Depends(get_database_session)):
    users = db.query(Users).filter(Users.id==users_id).first()
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="users is not found")
    return users

@router.post("/users/create",status_code=status.HTTP_201_CREATED)
def create_users(user:UsersIN,db:Session=Depends(get_database_session)):
    # hash the password 
    hashed_password = hash(user.password)
    user.password = hashed_password
    users=Users(**user.dict())
    db.add(users)
    db.commit()
    db.refresh(users)
    return {"data":users, "message":"data posted successfully"}

@router.post("/users/login", status_code=status.HTTP_200_OK, response_model=Token)
def login_user(login_user:OAuth2PasswordRequestForm=Depends(), db:Session=Depends(get_database_session)):
    login = db.query(Users).filter(Users.email==login_user.username).first()
    if not login:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")
    if not verify:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credential")
    access_token = create_access_token(data={"user_id":login.id})
    return {"access_token":access_token, "token_type":"bearer", "message":"login successfully"}
    