import logging
from datetime import datetime

# Log formatını ve seviyesini ayarlıyoruz
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(f"logs/app_{datetime.now().date()}.log"),  # Günlük log dosyası
        logging.StreamHandler()  # Konsola log yazma
    ]
)

# Logger nesnesi
logger = logging.getLogger("app_logger")

# Log fonksiyonları
def log_info(message: str):
    logger.info(message)

def log_error(message: str):
    logger.error(message)

def log_warning(message: str):
    logger.warning(message)
