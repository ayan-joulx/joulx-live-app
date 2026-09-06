from fastapi import FastAPI

app = FastAPI(
    title="Joulx Enterprise Control Tower",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {"status": "online", "message": "Joulx Enterprise Control Tower is running smoothly on Vercel!"}

# Agar tumhare aur bhi routes (endpoints) hain, woh sab yahan niche aa jayenge: