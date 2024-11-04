from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from uuid import uuid4, UUID

app = FastAPI()

class TodoCreate(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False

class Todo(TodoCreate):
    id: UUID

# In-memory database
todos = []

@app.post("/todos/", response_model=Todo)
async def create_todo(todo: TodoCreate):
    new_todo = Todo(id=uuid4(), **todo.dict())
    todos.append(new_todo)
    return new_todo

@app.get("/todos/", response_model=List[Todo])
async def read_todos():
    return todos

@app.get("/todos/{todo_id}", response_model=Todo)
async def read_todo(todo_id: UUID):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")

@app.put("/todos/{todo_id}", response_model=Todo)
async def update_todo(todo_id: UUID, updated_todo: TodoCreate):
    for todo in todos:
        if todo.id == todo_id:
            todo.title = updated_todo.title
            todo.description = updated_todo.description
            todo.completed = updated_todo.completed
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")

@app.delete("/todos/{todo_id}", response_model=dict)
async def delete_todo(todo_id: UUID):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos.pop(index)
            return {"message": "Todo deleted successfully"}
    raise HTTPException(status_code=404, detail="Todo not found")
