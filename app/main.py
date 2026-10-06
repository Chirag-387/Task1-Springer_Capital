from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import httpx

class BulkJobRequest(BaseModel):
    object_name: str
    operation: str

app = FastAPI()

stored_records = []

@app.post("/bulk-jobs/{job_id}/results")
def fetch_and_store_results(job_id: str):
    try:
        response = httpx.get(f"http://127.0.0.1:8001/jobs/{job_id}/results")
        response.raise_for_status()
        records = response.json()["records"]
    except httpx.HTTPStatusError:
        raise HTTPException(status_code=502, detail="Mock Salesforce returned an HTTP error")
    except httpx.RequestError:
        raise HTTPException(status_code=503, detail="Cannot reach mock Salesforce")

    stored_records.extend(records)
    return {"job_id": job_id, "stored_count": len(records)}


@app.get("/stored-records")
def list_stored_records():
    return stored_records


@app.get("/")
def home():
    return {"message": "Backend is running"}

@app.post("/bulk-jobs")
def test_salesforce(request: BulkJobRequest):
    try:
        response = httpx.post("http://127.0.0.1:8001/jobs", 
                              json = {
                                  "object_name": request.object_name,
                                  "operation": request.operation
                              })
        response.raise_for_status()
        return response.json()
    except httpx.HTTPStatusError:
        return {"error": "Mock Salesforce returned an HTTP error"}

@app.get("/bulk-jobs/{job_id}")
def get_bulk_job_status(job_id: str):
    try:
        response = httpx.get(f"http://127.0.0.1:8001/jobs/{job_id}")
        response.raise_for_status()
        return response.json()
    except httpx.HTTPStatusError:
        raise HTTPException(status_code=502, detail="Mock Salesforce returned an HTTP error")
    except httpx.RequestError:
        raise HTTPException(status_code=503, detail="Cannot reach mock Salesforce")