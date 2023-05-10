from passlib.context import CryptContext
from jose import jwt,JWTError
from datetime import datetime,timedelta
from .schemas import TokenData
# from fastapi import HTTPException,status,Depends
from fastapi.security import OAuth2PasswordBearer

oauth_schema = OAuth2PasswordBearer(tokenUrl="users/login")

#hashing the password
pwd_content = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash(password:str):
    return pwd_content.hash(password)

def verify(plain_password, hashed_password):
    return pwd_content.verify(plain_password, hashed_password)

#for jwt token

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563cc3f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data:dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# def verify_access_token(token:str,credentials_exception):
#     try:
#         payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
#         id : str =payload.get("user_id")
#         if id is None:
#             raise credentials_exception
#         token_data = TokenData(id=id)
#     except JWTError:
#         raise credentials_exception
#     return token_data

# def get_current_user(token:str=Depends(oauth_schema)):
#     credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
#                             detail=f'could not found validate credtionals',headers={"www-Authenticate":"Bearer"})
#     return verify_access_token(token,credentials_exception)