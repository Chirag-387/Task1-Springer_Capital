from fastapi import FastAPI

app = FastAPI()

@app.post("/jobs")
def create_job():
    return {
        "job_id": "mock-job-001",
        "status": "created"
    }
