from motor.motor_asyncio import AsyncIOMotorClient
from .config import settings

# MongoDB istemcisini tanımlar ve bağlanır
client = AsyncIOMotorClient(settings.mongodb_uri)
database = client[settings.database_name]

def get_database():
    return database
