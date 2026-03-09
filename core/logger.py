import logging
import os
from pathlib import Path

LOG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
formatter = logging.Formatter(LOG_FORMAT)

logger = logging.getLogger('Bloom')
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

log_dir = Path('/app/logs')
log_file = log_dir / 'app.log' if os.access(log_dir, os.W_OK) else Path('app.log')

try:
    file_handler = logging.FileHandler(log_file, encoding='utf-8')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
except (PermissionError, OSError):
    pass