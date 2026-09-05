import os
import random
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="Joulx Enterprise Control Tower")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class SignupRequest(BaseModel):
    company: str
    email: str

class OptimizationRequest(BaseModel):
    api_key: str
    sparsity: int
    architecture: str

@app.post("/api/signup")
def register_company(data: SignupRequest):
    generated_key = f"joulx_live_{random.randint(100000, 999999)}"
    return {
        "status": "SUCCESS",
        "company": data.company,
        "api_key": generated_key,
        "tier": "Enterprise Level-1"
    }

@app.post("/api/optimize")
def optimize_model(data: OptimizationRequest):
    if not data.api_key.startswith("joulx_"):
        raise HTTPException(status_code=400, detail="Invalid API Key")
    
    saved_power = round(data.sparsity * 0.76, 2)
    return {
        "status": "OPTIMIZED",
        "sparsity": f"{data.sparsity}%",
        "active_tensors": f"{int(2048 * (1 - data.sparsity/100))} / 2048",
        "power_saved": f"{saved_power} kW/h",
        "message": f"Successfully calibrated weights for {data.architecture} architecture."
    }

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("app:app", host="0.0.0.0", port=port)