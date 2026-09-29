from fastapi import FastAPI
import httpx

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Backend is running"}

@app.post("/test-salesforce")
def test_salesforce():
    try:
        response = httpx.post("http://127.0.0.1:8001/jobs")
        response.raise_for_status()
        return response.json()
    except httpx.HTTPStatusError:
        return {"error": "Mock Salesforce returned an HTTP error"}