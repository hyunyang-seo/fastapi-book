from pydantic import BaseModel

class Todo(BaseModel):
    id: int
    item: str 
    
    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "item": "Example todo item."
            }
        }
        
class TodoItem(BaseModel):
    item: str
    
    class Config:
        json_schema_extra = {
            "example": {
                "item": "Read the next chapter of the book."
            }
        }
        
class TodoItems(BaseModel):
    todos: list[TodoItem]
    
    class Config:
        json_schema_extra = {
            "example": {
                "todos": [
                    {
                        "item": "Example schema 1!"
                    },
                    {
                        "item": "Example schema 2!"
                    }
                ]
            }
        }
        

        
        


    
