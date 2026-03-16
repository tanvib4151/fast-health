from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from datetime import date

#start
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,  # IMPORTANT
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

@app.post("/onboarding_tracking-points/{user_id}")
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


daily_logs_db={
    "2026-03-12":[
    {
      "subpoint": "Nausea",
      "duration": "<hour",
      "intensity": 1,
      "factors": "milk",
      "impact": "High",
      "other": "I'm so nauseous it makes me want to throw up and I can't eat anything",
    },
    {
      "subpoint": "Pain",
      "duration": "1_hour",
      "intensity": 5,
      "factors": "walking",
      "impact": "High",
      "other": "I have pain all over my body and it makes it hard to do anything and I can't sleep",
    },
    {
      "subpoint": "Headache",
      "duration": "3_hour",
      "intensity": 5,
      "factors": "Lack of Sleep",
      "impact": "High",
      "other": "I go to sleep and the headache is really bad and affects my sleep and makes me very sad",
    },
    {
      "subpoint": "Fatigue",
      "duration": "6_hour",
      "intensity": 2,
      "factors": "Lack of Sleep",
      "impact": "High",
      "other": "I go to sleep and the fatigue is really bad and affects my sleep and makes me very sad",
    }
    ],
    "2026-03-13":[
    {
      "subpoint": "Nausea",
      "duration": "<hour",
      "intensity": 1,
      "factors": "water",
      "impact": "High",
      "other": "I'm so nauseous it makes me want to throw up and I can't eat anything",
    },
    {
      "subpoint": "Pain",
      "duration": "1_hour",
      "intensity": 5,
      "factors": "walking",
      "impact": "High",
      "other": "I have pain all over my body and it makes it hard to do anything and I can't sleep",
    },
    {
      "subpoint": "Headache",
      "duration": "3_hour",
      "intensity": 5,
      "factors": "Lack of Sleep",
      "impact": "High",
      "other": "I go to sleep and the headache is really bad and affects my sleep and makes me very sad",
    },
    {
      "subpoint": "Fatigue",
      "duration": "6_hour",
      "intensity": 2,
      "factors": "Lack of Sleep",
      "impact": "High",
      "other": "I go to sleep and the fatigue is really bad and affects my sleep and makes me very sad",
    }
    ]

}
@app.get("/dailylog/{log_date}")

def get_daily_log(log_date: str):
    if not validate_date(log_date):
        return {"error": "Invalid date format. Please use YYYY-MM-DD."}
    
    logs = daily_logs_db.get(log_date, [])
    return{
  "date": log_date,
  "logs": logs
    }
def validate_date(date_str: str) -> bool:
    try:
        date.fromisoformat(date_str)
        return True
    except ValueError:
        return False 

#yyyy-MM-dd
# first vaildate string is in correct format and then return the daily log for that date