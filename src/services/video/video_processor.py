# src/services/video/video_processor.py
import cv2

class VideoProcessor:
    def __init__(self, video_path):
        self.video_path = video_path
        self.cap = cv2.VideoCapture(video_path)

    def get_frame_count(self):
        return int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))

    def get_fps(self):
        return int(self.cap.get(cv2.CAP_PROP_FPS))

    def read_frames(self):
        frames = []
        while self.cap.isOpened():
            ret, frame = self.cap.read()
            if not ret:
                break
            frames.append(frame)
        self.cap.release()
        return frames
