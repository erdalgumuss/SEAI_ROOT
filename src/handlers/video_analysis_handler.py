# src/handlers/video_analysis_handler.py
from src.services.video.video_processor import VideoProcessor
from src.services.video.face_recognition import FaceRecognition
from src.services.video.emotion_analysis import EmotionAnalysis

class VideoAnalysisHandler:
    def __init__(self, video_path):
        self.video_processor = VideoProcessor(video_path)
        self.face_recognition = FaceRecognition()
        self.emotion_analysis = EmotionAnalysis()

    async def analyze_video(self, request, db):
        # Video analizini burada tanımlayın
        frames = self.video_processor.read_frames()
        results = []
        for frame in frames:
            faces = self.face_recognition.detect_faces(frame)
            for (x, y, w, h) in faces:
                face_img = frame[y:y+h, x:x+w]
                emotion = self.emotion_analysis.predict_emotion(face_img)
                results.append({
                    "face_coordinates": (x, y, w, h),
                    "emotion": emotion
                })
        return results
