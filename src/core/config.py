from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()  # .env dosyasındaki çevresel değişkenleri yükler

class Settings(BaseSettings):
    mongodb_uri: str = os.getenv("MONGODB_URI")
    database_name: str = os.getenv("DATABASE_NAME")

settings = Settings()
