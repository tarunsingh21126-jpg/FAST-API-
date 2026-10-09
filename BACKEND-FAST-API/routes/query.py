from pydantic import BaseModel

from fastapi import APIRouter,status,HTTPException,Request,Depends,Header
from fastapi.responses import  JSONResponse
query = APIRouter()


users = []
class user(BaseModel):
    name :str
    age:int
    password:str

class UserResponse(BaseModel):
    name:str
    age:int
#STATUS CODE AND RESPONSE
@query.post("/post_status",status_code=status.HTTP_201_CREATED)
def create_user():
    return{
        "message":"USER Created"
    }
@query.get("/status_userget")
def get_user():
    return{
        "status":"sucess",
        "message":"uSER FETCH",
        "data" : {
            "name":"tarun",
            "age":24
        }
    }
# BASIC ERROR VALIDATION AND CHECK
@query.get("/error_userget/{user_id}")
def get_user(user_id:int):
    if user_id != 1:
        raise HTTPException(
            status_code=404,
            detail = "User not found"
        )
    return{
        "id":1,
        "name":"tarun",
        "age":24      
    }
# RESPONSE HANDLNG
@query.get("/response_user", response_model=UserResponse)
def get_user():
    return {
        "name":"TARUN",
        "age":24,
        "password":"1234567"
    }
    
#QUERY HANDLING
@query.post("/qpost")
def quser(q:user):
    users.append(q)
    return {
        "message":"QUERY CREATED",
        "data":q
    }
    
@query.put("/qput/{user_id}")
def update_user(user_id: int, user: user, notify: bool = False):
    if user_id < len(users):
        users[user_id] = user
        return {
            "message": "USER UPDATED",
            "notify": notify,
            "data": user
        }

    return {
        "error": "USER NOT FOUND"
    }

#CUSTOM EXCEPTION HANDLING .\venv\Scripts\Activate.ps1      python -m uvicorn main:app --reload

class UserNOTFoundException(Exception):
    def __init__(self,name:str):
        self.name = name

@query.get("/cusers/{name}")
def get_user(name:str):
    if name!= "mohit":
        raise UserNOTFoundException(name)
    return {
        "name":name
    }

#DEPENDS INJECTION
def common_logic():
    return{
        "message":"COMMON LOGIC EXECUTED"
    }
@query.get("/HOMEA")
def home(data = Depends(common_logic)):
    return data

#resuable logic
def get_currentuser():
    return{
        "user":"Mohit"
    }

@query.get("/profileuser")
def profile(user = Depends(get_currentuser)):
    return user

@query.get("/dasuser")
def dasuser(user = Depends(get_currentuser)):
    return user


#auth intro

def varify_token(token:str =Header(None)):
    if token != "mysecret-token":
        raise HTTPException(
            status_code = 401,
            detail = "Unauthorized"
        )
    return {
        "user":"AUTHORIZED USER"
    }

@query.get("/securedata")
def securedata(user = Depends(varify_token)):
    return{
        "message":"secure data acessed",
        "user":user

    }

