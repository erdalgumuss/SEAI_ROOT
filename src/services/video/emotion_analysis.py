from tensorflow.keras.models import load_model
import cv2
import numpy as np

class EmotionAnalysis:
    def __init__(self, model_path="path/to/emotion_model.h5"):
        self.model = load_model(model_path)
        self.emotions = ["Angry", "Disgust", "Fear", "Happy", "Sad", "Surprise", "Neutral"]

    def predict_emotion(self, face_image):
        face_image = cv2.resize(face_image, (48, 48))
        face_image = face_image.astype("float32") / 255
        face_image = np.expand_dims(face_image, axis=0)
        prediction = self.model.predict(face_image)
        emotion_label = self.emotions[np.argmax(prediction)]
        return emotion_label
