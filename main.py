from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,  # IMPORTANT
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
def root():
    return {"message": "hi"}

class Person(BaseModel):
    FirstName: str
    LastName: str
    Email: str
    Password: str

@app.post("/")
def register (person: Person):
    return {"FirstName": person.FirstName, "LastName": person.LastName, "Email": person.Email, "Password": person.Password}

@app.post("/onboarding_trackingpoints/{user_id}")
def onboarding_trackingpoints(user_id: int, tracking_points: dict):
    return {
        "user_id": user_id,
        "tracking_points": tracking_points
    }

@app.get("/tracking-points/{user_id}")
def get_tracking_points(user_id: int):
    return{
  "tracking_points": [
    {
      "id": "tp_1",
      "type": "symptom",
      "user_selected": True
    },
    {
      "id": "tp_2",
      "type": "factor",
      "user_selected": False
    },
    {
      "id": "tp_3",
      "type": "treatment",
      "user_selected": False
    },
    {
      "id": "tp_4",
      "type": "mood",
      "user_selected": False
    }
  ]
}

@app.get("/subpoints")

def get_subpoints():
    return{
  "subpoints": [
    {
      "id": "s1",
      "name": "Headache",
      "user_selected": True,
    },
    {
      "id": "s2",
      "name": "Nausea",
      "user_selected": False,
    },
    {
      "id": "s3",
      "name": "Pain",
      "user_selected": False,
    },
    {
      "id": "s4",
      "name": "Fatigue",
      "user_selected": False,
    }
  ]
}