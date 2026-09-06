from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import random
import os

app = FastAPI(
    title="Joulx Enterprise Control Tower",
    version="1.0.0"
)

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

@app.get("/", response_class=HTMLResponse)
def read_root():
    # Yeh code root URL par seedha hamara index.html dashboard dikhayega
    if os.path.exists("index.html"):
        with open("index.html", "r", encoding="utf-8") as f:
            return f.read()
    return {"status": "online", "message": "Joulx Enterprise Control Tower API is running!"}

@app.post("/api/signup")
def handle_signup(data: SignupRequest):
    generated_key = f"joulx_live_sec_{random.randint(100000, 999999)}bc10"
    return {
        "status": "success",
        "message": f"Welcome {data.company_name}! Enterprise credentials provisioned.",
        "api_key": generated_key
    }

@app.post("/api/optimize")
def handle_optimize(data: OptimizeRequest):
    active_tensors_count = int(2048 * (1 - (data.sparsity / 100)))
    power_saved_val = round(data.sparsity * 0.77, 2)
    
    return {
        "status": "success",
        "sparsity": f"{data.sparsity}%",
        "active_tensors": f"{active_tensors_count} / 2,048",
        "power_saved": f"{power_saved_val} kW/h",
        "message": f"Successfully optimized model weights for {data.industry} under {data.deployment} architecture."
    }