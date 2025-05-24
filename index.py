from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

with open("marks.json", "r") as f:
    marks_data = json.load(f)

@app.get("/")
async def get_marks(request: Request):
    names = request.query_params.getlist("name")
    result = [marks_data.get(name, None) for name in names]
    return JSONResponse(content={"marks": result})
