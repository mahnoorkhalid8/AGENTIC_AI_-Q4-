from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, validator, constr
from typing import Optional, List, Dict
from typing import Annotated
from datetime import date

app = FastAPI()
USERS: Dict[int, "UserRead"] = {}
TASKS: Dict[int, "Task"] = {}

user_id_counter = 1
tasks_id_counter =1

class UserCreate(BaseModel):
    name: Annotated[str, constr(min_length=3, max_length=20)]
    email: EmailStr
    
class UserRead(BaseModel):
    id: int
    name: str
    email: EmailStr
    
class Task(BaseModel):
    id: int
    user_id: int
    title: str
    description: Optional[str] = None
    status: Optional[str] = "pending"
    due_date: date
    
    @validator("due_date")
    def validate_due_date(cls, v):
        if v < date.today:
            raise ValueError("Due date must be today or in the future.")
        return v
    
class TaskCreate(Task):
    id: int
    
# Root endpoint
@app.get("/")
async def read_root():
    return {"message": "Welcome to the Task Tracker API"}

# User endpoints

# Create a user (return UserRead)
@app.post("/users", response_model=UserRead)
def create_user(user: UserCreate):
    global user_id_counter
    
    user_data = user.dict()
    user_data["id"] = user_id_counter
    USERS[user_id_counter] = UserRead(**user_data)
    user_id_counter += 1
    return USERS[user_id_counter - 1]
    
# Retrieve user
@app.get("/users/{user_id}", response_model=UserRead)
def get_user(user_id:int):
    user = USERS.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# Task endpoint

# Create a task (return full task model)
@app.post("/tasks/", response_model=Task)
def create_task(task: TaskCreate):
    global tasks_id_counter
    
    if task.user_id not in USERS:
        raise HTTPException(status_code=404, detail="User not found.")
    
    task_data = task.dict()
    task_data["id"] = tasks_id_counter
    TASKS[tasks_id_counter] = Task(**task_data)
    tasks_id_counter += 1
    return task_data
    
    # task.id = len(TASKS) + 1
    # TASKS[task.id] = task
    # return task
    
# Get task
@app.get("/tasks/{tasks_id}", response_model=Task)
def get_task(task_id: int):
    task = TASKS.get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

# Update status only, vaalidating allowed values
@app.put("/tasks/{tasks_id}", response_model=Task)
def update_task(task_id: int, status: str):
    allowed_status = ["pending", "in_progress", "done"]
    if status not in allowed_status:
        raise HTTPException(status_code=404, detail=f"Status must be one of {allowed_status}")
    
    task = TASKS.get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    task.status = status
    return task

# List of tasks
@app.get("/users/{user_id}/tasks", response_model=List[Task])
def list_user_tasks(user_id: int):
    if user_id not in USERS:
        raise HTTPException(status_code=404, detail="User not found.")
    
    user_tasks = [task for task in TASKS.values() if task.user_id == user_id]
    return user_tasks