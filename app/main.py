from fastapi import FastAPI

app = FastAPI(title="Weather API", version="1.0.0")

@app.get("/")
async def root():
    return {"message": "Weather API Service"}