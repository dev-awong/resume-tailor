from fastapi import APIRouter
from pydantic import BaseModel
from app.services.ai_tailor import tailor_resume

router = APIRouter()

class TailorRequest(BaseModel):
    resume_text: str
    job_keywords: list[str]

@router.post("/tailor")
def tailor(request: TailorRequest):
    tailored = tailor_resume(request.resume_text, request.job_keywords)
    return {"tailored_resume": tailored}

