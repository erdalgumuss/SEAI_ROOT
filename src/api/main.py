from fastapi import FastAPI
from .routes.video_analysis import router as video_analysis_router
from src.core.dependencies import get_database

app = FastAPI()

# API route'ları ekleyin
app.include_router(video_analysis_router, prefix="/api")

# Başlangıç ve kapanış işlemleri
@app.on_event("startup")
async def startup_db_client():
    print("Connecting to MongoDB...")

@app.on_event("shutdown")
async def shutdown_db_client():
    print("Shutting down MongoDB connection...")
    get_database().client.close()
