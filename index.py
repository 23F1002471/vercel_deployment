from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# Load marks.json once (adjust path if needed)
with open('marks.json') as f:
    marks_list = json.load(f)

# Convert list of dicts to dict: {name: marks}
marks_data = {entry['name']: entry['marks'] for entry in marks_list}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for CORS
    allow_methods=["GET"],
    allow_headers=["*"],
)

@app.get("/api")
async def get_marks(request: Request):
    names = request.query_params.getlist("name")  # Get all ?name= params
    result = [marks_data.get(name, None) for name in names]  # Lookup marks or None
    return {"marks": result}
