from pydantic import BaseModel
import numpy as np

# Frontend se aane wale Signup data ke liye model
class SignupRequest(BaseModel):
    company_name: str
    work_email: str
    industry: str

# Frontend se aane wale Optimization request ke liye model
class OptimizationRequest(BaseModel):
    api_key: str
    target_sparsity: float = 0.5

# 1. Signup Endpoint: Jab client register karega
@app.post("/api/signup")
async def enterprise_signup(data: SignupRequest):
    # Yahan hum client ke liye ek unique enterprise API key generate kar rahe hain
    mock_api_key = "jx_live_" + np.random.bytes(8).hex()
    
    return {
        "status": "success",
        "message": f"Welcome {data.company_name}! Account created successfully.",
        "assigned_industry": data.industry,
        "api_key": mock_api_key,
        "deployment_ready": True
    }

# 2. Optimization Endpoint: Jab client AI weights optimize karega
@app.post("/api/optimize")
async def run_optimization(payload: OptimizationRequest):
    # Dummy AI weights par thermodynamic optimization run kar rahe hain
    arr = np.array([1.2, -2.5, 0.3, 0.7, -1.9, 0.4])
    threshold = np.percentile(np.abs(arr), payload.target_sparsity * 100)
    mask = np.abs(arr) >= threshold
    optimized_weights = arr * mask
    saved_energy_kwh = float(np.sum(np.abs(arr)) * 0.075)
    
    return {
        "status": "success",
        "target_sparsity": f"{payload.target_sparsity * 100}%",
        "active_weights_count": int(np.sum(mask)),
        "optimized_weights": optimized_weights.tolist(),
        "estimated_energy_saved_kwh": round(saved_energy_kwh, 4),
        "cost_reduction_percent": 50.0
    }