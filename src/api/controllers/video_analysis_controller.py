from fastapi import APIRouter, HTTPException, Depends
from src.core.dependencies import get_database
from src.models.video_analysis_request import VideoAnalysisRequest
from src.handlers.video_analysis_handler import VideoAnalysisHandler
from pymongo.errors import ServerSelectionTimeoutError

router = APIRouter()

@router.post("/analyze", summary="Video analizi başlatır")
async def analyze_video(request: VideoAnalysisRequest, db=Depends(get_database)):
    try:
        # Her istekte yeni bir VideoAnalysisHandler oluşturun
        handler = VideoAnalysisHandler(video_path=request.video_path)
        
        # Handler aracılığıyla video analizini başlat
        result = await handler.analyze_video(request, db)
        return {"status": "success", "data": result}
    except ServerSelectionTimeoutError:
        raise HTTPException(status_code=500, detail="MongoDB bağlantı hatası")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
