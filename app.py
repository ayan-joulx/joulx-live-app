from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import random

app = FastAPI(
    title="Joulx Enterprise Control Tower",
    version="1.0.0"
)

# CORS setup taake frontend request block na ho
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class SignupRequest(BaseModel):
    company_name: str
    work_email: str

class OptimizeRequest(BaseModel):
    api_key: str
    company_name: str
    industry: str
    deployment: str
    sparsity: float

@app.get("/")
def read_root():
    return {"status": "online", "message": "Joulx Enterprise Control Tower is running successfully!"}

@app.post("/api/signup")
def handle_signup(data: SignupRequest):
    # Generate a dummy secure API key for the enterprise tenant
    generated_key = f"joulx_live_sec_{random.randint(100000, 999999)}bc10"
    return {
        "status": "success",
        "message": f"Welcome {data.company_name}! Enterprise credentials provisioned.",
        "api_key": generated_key
    }

@app.post("/api/optimize")
def handle_optimize(data: OptimizeRequest):
    # Calculate simulated metrics based on sparsity ratio
    active_tensors_count = int(2048 * (1 - (data.sparsity / 100)))
    power_saved_val = round(data.sparsity * 0.77, 2)
    
    return {
        "status": "success",
        "sparsity": f"{data.sparsity}%",
        "active_tensors": f"{active_tensors_count} / 2,048",
        "power_saved": f"{power_saved_val} kW/h",
        "message": f"Successfully optimized model weights for {data.industry} under {data.deployment} architecture."
    }