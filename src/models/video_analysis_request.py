from pydantic import BaseModel, HttpUrl

class VideoAnalysisRequest(BaseModel):
    video_url: HttpUrl
    analyze_faces: bool = True  # Yüz tanıma analizini etkinleştirmek için
    analyze_emotions: bool = False  # Duygu analizini etkinleştirmek için
