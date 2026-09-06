import os
import uvicorn
from fastapi import FastAPI

# FastAPI app initialization
app = FastAPI(
    title="Joulx Enterprise Control Tower",
    version="1.0.0"
)

# Root route taake / par 502 error na aaye aur aik basic message dikhe
@app.get("/")
def read_root():
    return {"status": "online", "message": "Joulx Enterprise Control Tower is running successfully!"}

# Aapke baaki ke saare routes aur endpoints yahan aage aayenge...


# Yeh block automatically Railway ke diye hue port ko utha lega
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run("app:app", host="0.0.0.0", port=port)