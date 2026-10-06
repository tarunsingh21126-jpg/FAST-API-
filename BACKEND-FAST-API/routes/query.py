from pydantic import BaseModel

from fastapi import APIRouter
query = APIRouter()


users = []
class user(BaseModel):
    name :str
    age:int

@query.post("/q")
def quser(q:user):
    users.append(q)
    return {
        "message":"QUERY CREATED",
        "data":q
    }
    
@query.put("/q/{user_id}")
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

