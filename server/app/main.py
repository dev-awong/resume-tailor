from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import job, resume

app = FastAPI()

# Allow frontend (Next.js) to reach API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to your production domain later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(job.router, prefix="/api/job")
app.include_router(resume.router, prefix="/api/resume")

@app.get("/")
def root():
    return {"message": "Resume Tailor Backend Running!"}

