from fastapi import FastAPI
from src.controllers import gist_controller


app = FastAPI(
    title="Gist Weather API",
    description="Api de clima integrada ao Gist",
    version="1.0.0"
)

app.include_router(gist_controller.router)

@app.get("/")
async def root():
    return {"message": "Welcome to Weather API!"}