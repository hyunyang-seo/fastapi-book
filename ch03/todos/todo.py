from fastapi import APIRouter, Path, HTTPException, status
from model import Todo, TodoItem, TodoItems

todo_router = APIRouter()

todo_list = []

@todo_router.post("/todo", status_code=status.HTTP_201_CREATED)
async def add_todo(todo: Todo) -> dict:
    todo_list.append(todo)
    return {
        "mesage": "Todo added successfully."
    }
    
@todo_router.get("/todo", response_model=TodoItems)
async def retrieve_todos() -> dict:
    return {
        "todos": todo_list
    }
    
@todo_router.get("/todo/{todo_id}")
async def get_single_todo(todo_id: int) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            return {
                "todo": todo
            }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Todo with given id not found."
    )

@todo_router.put("/todo/{todo_id}")
async def update_todo(todo_data: TodoItem, 
                      todo_id: int = Path(..., title = "The ID of the todoto be updated.")) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            todo.item = todo_data.item
            return {
                "message": "Todo updated successfully."
            }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Todo with given id not found."
    )
    
    
@todo_router.delete("/todo")
async def delete_all_todos() -> dict:
    todo_list.clear()
    return {
        "message": "All todos deleted successfully."
    }
    
    
@todo_router.delete("/todo/{todo_id}")
async def delete_single_todo(todo_id: int) -> dict:
    for index in range(len(todo_list)):
        todo = todo_list[index]
        if todo_id == todo.id:
            todo_list.pop(index)
            return {
                "message": "Todo deleted successfully."
            }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Todo with given id not found."
    )
    
