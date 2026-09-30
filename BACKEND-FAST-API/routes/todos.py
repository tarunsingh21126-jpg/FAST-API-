from pydantic import BaseModel

from fastapi import APIRouter
router = APIRouter()



todos = []
class Todo(BaseModel):
    id:int
    title:str
    completed:bool

@router.post("/todos")
def create_todos(todo:Todo):
    todos.append(todo)
    return {
        "message":"TODO ADDED",
        "data":todo
    }
@router.get("/todos")
def get_todos():
    return todos
@router.get("/todos/{todo_id}")
def get_todo(todo_id:int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    return {"ERROR:TODO NOT FOUND"}