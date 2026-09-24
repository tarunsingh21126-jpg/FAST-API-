from fastapi import FastAPI

app = FastAPI()

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