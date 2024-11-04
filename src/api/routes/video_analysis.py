from fastapi import APIRouter
from src.api.controllers.video_analysis_controller import router as video_analysis_controller

router = APIRouter()
router.include_router(video_analysis_controller, prefix="/video", tags=["Video Analysis"])
