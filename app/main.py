from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Todo(BaseModel):
    id:        int
    title:     str
    completed: bool

class TodoCreate(BaseModel):
    title:     str
    completed: bool = False

class TodoUpdate(BaseModel):
    id:        int
    title:     str  | None = None
    completed: bool | None = None

todo_id: int = 0
todos: list[Todo] = []

@app.post("/todo")
def create_todo(todo: TodoCreate):
    new_todo = Todo(
        id=todo_id + 1,
        title=todo.title,
        completed=todo.completed
    )

    todos.append(new_todo)

    return {
        "success": "true"
    }

@app.get("/todo", response_model=list[Todo])
def get_all_todos():
    return todos

@app.patch("/todo")
def update_todo(todo: TodoUpdate):
    for x in todos:
        if x.id == todo.id:
            if(not todo.title == None):
                x.title = todo.title
            
            if(not todo.completed == None):
                x.completed = todo.completed
            
            return {
                "success": "true"
            }
    
    return {
        "message": "Todo not found"
    }

@app.delete("/todo")
def delete_todo(id: int):
    for x in todos:
        if x.id == id:
            todos.remove(x)

            return {
                "success": "true"
            }
    
    return {
        "message": "Todo not found"
    }