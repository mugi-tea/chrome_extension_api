from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

settings = json.load(open('settings.json', encoding='utf-8'))

@app.get("/")
def index(value: str):
  match value:
    case "":
      return settings
    
    case "engineering_department":
      return settings["common"], settings["engineering_department"]
    
    case "planning_department":
      return settings["common"], settings["planning_department"]
      