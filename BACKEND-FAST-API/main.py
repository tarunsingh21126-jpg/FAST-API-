from fastapi import FastAPI,status
from pydantic import BaseModel
app = FastAPI()
class User(BaseModel):
    name:str
    age:int
# HOME PAGE 
@app.get("/")
def home():
    return {"message":"hello fastapi"}

# ABOUT PAGE
@app.get("/about")
def about():
    return {"message":"TARUN SINGH"}

# USERS NAMES

@app.get("/users/{user_id}")
def users(user_id:int):
    return {
        "user_id": user_id
    }

@app.get("/users")
def get_users(name: str = None):
    return {"Name": name}

@app.get("/products")
def get_users(limit:int = 10):
    return {"limit":limit}

@app.get("/items")
def get_users(name:str=None,price:int=0):
    return {
        "name":name,
        "price":price
    }

#post request

@app.post("/cr-user")
def create_user(name:str,age:int):
    return {
        "name":name,
        "age":age
    }

#through json format
@app.post("/sign-user")
def create_user(user:dict):
    return {
        "message":"DATA CREATED SUCESSFULLY",
        "data":user
    }

#with validation example of pydantic
@app.post("/sign-up")
def create_user(user:User):
    return {
        "message":"DATA CREATED SUCESSFULLY pydantic",
        "data":user
    }

# pydantic scheme structure

# class User(BaseModel):
#     name:str
#     age:int
#     address:Address

# @app.post("/create_user")
# def create_user(user:User):
#     return {
#         "meassage":"User Created sucessfully",
#         "data":user
#     }
# nested models

class Address(BaseModel):
    city:str
    pincode:int

class User(BaseModel):
    name:str
    age:int
    address:Address

# @app.post("/create_user")
# def create_user(user:User):
#     return {
#         "meassage":"User Created sucessfully",
#         "data":user
#     }

#CRUD OPERATIONS 
from routes.todos import router as todo_router
app.include_router(todo_router)

# QUERY - PATH - BODY STRUCTURE
from routes.query import query
app.include_router(query)
