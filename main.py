from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
new_id = 1

class User_Info(BaseModel):
    username: str
    password: str
    email: str 
    is_active: bool

class User_update(BaseModel):
    username: str
    email: str 
    is_active: bool

class LoginRequest(BaseModel):
    email: str
    password: str

users = []

@app.post("/register")
def create_user(user: User_Info):
    global new_id
    for unique in users:
        if unique["username"] == user.username:
            return {"message": "Username already exists"}
    
    new_user = {
        "id": new_id,
        "username": user.username,
        "password": user.password,  
        "email": user.email,
        "is_active": user.is_active
    }
    users.append(new_user)
    new_id += 1
    return new_user

@app.get("/List") 
def list_users(): 
    return users

@app.get("/Search")
def get_user(id: int):
    for unique_id in users:
        if unique_id["id"] == id:
            return {
                "User name": unique_id["username"],
                "User email": unique_id["email"],
                "Active": unique_id["is_active"]
            }
    return {"message": "User not found"}

@app.put("/Update")
def update_user(id: int, user: User_update):
    for unique_id in users:
        if unique_id["id"] == id:
            unique_id["username"] = user.username
            unique_id["email"] = user.email
            unique_id["is_active"] = user.is_active
            return {"message": "User successfully updated", "user": unique_id}
    return {"message": "User not found"}

@app.delete("/Delete")
def delete_user(id: int):
    for unique_id in users:
        if unique_id["id"] == id:
            users.remove(unique_id)
            return {"message": "User deleted successfully"}
    return {"message": "User not found"}

@app.post("/Login")
def login(request: LoginRequest):
    for unique_id in users:
        if request.email == unique_id["email"] and request.password == unique_id["password"]:
            return {"message": "Successful login"}
    return {"message": "Something went wrong when logging"}