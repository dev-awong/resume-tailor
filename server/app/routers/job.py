from fastapi import APIRouter
from pydantic import BaseModel
from app.services.job_parser import extract_keywords

router = APIRouter()

class JobInput(BaseModel):
    job_description: str

@router.post("/analyze")
def analyze_job(input: JobInput):
    keywords = extract_keywords(input.job_description)
    return {"keywords": keywords}

