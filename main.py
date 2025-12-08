from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

class Person(BaseModel):
    FirstName: str
    LastName: str
    Email: str
    Password: str

@app.post("/")
def register (person: Person):
    return {"FirstName": person.FirstName, "LastName": person.LastName, "Email": person.Email, "Password": person.Password}
