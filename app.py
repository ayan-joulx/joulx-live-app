from fastapi import FastAPI

app = FastAPI(
    title="Joulx Enterprise Control Tower",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {"status": "online", "message": "Joulx Enterprise Control Tower is running successfully!"}