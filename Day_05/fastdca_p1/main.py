from fastapi import FastAPI, Depends, Query, HTTPException, status
from typing import Annotated

app = FastAPI()

# Simple Dependency
def get_simple_dependency():
    return {"goal": "We are building AI gents Workforce"}

@app.get("/get_simple_dependency")
def simple_dependency(response: Annotated[dict, Depends(get_simple_dependency)]):
    return response

# Dependency with parameter
def get_goal(username: str):
    return {"goal": "We are building AI gents Workforce", "username": username}

@app.get("/get-goal")
def get_my_goal(response: Annotated[dict, Depends(get_goal)]):
    return response

# Dependency with Query parameter
def login_dependency(username: str = Query(None), password: str = Query(None)):
    if username == "admin" and password == "admin":
        return {"message": "Login Successful"}
    else:
        return {"message": "Login Failed"}
    
@app.get("/signin")
def login_api(user: Annotated[dict, Depends(login_dependency)]):
    return user

# Multiple Dependencies
def depfunc1(num: int):
    num = int(num)
    num += 1
    return num

def depfunc2(num):
    num = int(num)
    num += 2
    return num

@app.get("/main/{num}")
def get_main(num: int, num1: Annotated[int, Depends(depfunc1)], num2: Annotated[int, Depends(depfunc2)]):
    
    # Assuming you want to use num1 and num2 in some way
    #        1     2      3
    total = num + num1 + num2
    return f"Pakistan {total}"

# Classes
blogs = {
    "1": "Generative AI Blog",
    "2": "Machine Learning Blog",
    "3": "Deep Learning Blog"
}

user = {
    "4": "Mahnoor",
    "8": "Khalid"
}

class GetObjectOr404():
    def __init__(self, model) -> None:
        self.model = model
        
    def __call__(self, id: str):
        obj = self.model.get(id)
        if not obj:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Object Id {id} not found")
        return obj
    
blog_dependency = GetObjectOr404(blogs)

@app.get("/blog/{id}")
def get_blog(blog_name: Annotated[str, Depends(blog_dependency)]):
    return blog_name

user_dependency = GetObjectOr404(user)

@app.get("/user/{id}")
def get_user(user_name: Annotated[str, Depends(user_dependency)]):
    return user_name