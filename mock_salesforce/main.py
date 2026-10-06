from fastapi import FastAPI
# from pydantic import BaseModel

# class BulkJobRequests(BaseModel):
#     object_name: str
#     operation: str

app = FastAPI()

@app.post("/jobs")
def create_job():
    return {
        "job_id": "mock-job-001",
        "status": "created"
    }

@app.get("/jobs/{job_id}")
def get_job_status(job_id: str):
    return {"job_id": job_id, "status": "completed"}


@app.get("/jobs/{job_id}/results")
def get_job_results(job_id: str):
    return {
        "job_id": job_id,
        "records": [
            {"id": "001", "name": "Acme Corp"},
            {"id": "002", "name": "Globex"},
        ],
    }