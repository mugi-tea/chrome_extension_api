from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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

settings = {
  "common": {
    "name":"共通",
    "items":[
      {
        "name": "GitHub",
        "url":"https://github.com/RonwareJP",
        "img_url":"https://cdn-icons-png.flaticon.com/512/25/25231.png"
      },
      {
        "name": "GitHub",
        "url":"https://github.com/RonwareJP",
      },
      {
        "name": "GitHub",
        "url":"https://github.com/RonwareJP"
      }
    ]
  },
  "engineering_department": {
    "name":"技術部門",
    "items": [
      {
        "name": "GitHub",
        "url":"https://github.com/RonwareJP",
      },
      {
        "name": "exciroute",
        "url":"https://exciroute.com/",
        "img_url":""
      },
      {
        "name": "GitHub",
        "url":"https://github.com/RonwareJP"
      }
    ]
  },
  "planning_department": {
    "name": "企画部門",
    "items": [
      {
        "name": "GitHub",
        "url":"https://github.com/RonwareJP"
      },
      {
        "name": "GitHub",
        "url":"https://github.com/RonwareJP"
      },
      {
        "name": "GitHub",
        "url":"https://github.com/RonwareJP"
      }
    ]
  }
}


@app.get("/")
def index(value: str):
  match value:
    case "":
      return settings
    
    case "engineering_department":
      return settings["common"], settings["engineering_department"]
    
    case "planning_department":
      return settings["common"], settings["planning_department"]
      