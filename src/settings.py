import os
from pathlib import Path

from dotenv import load_dotenv


# Создавайте пути внутри проекта следующим образом: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(os.path.join(BASE_DIR, '.env'))

TEAM_TOKEN = os.getenv('TEAM_TOKEN')
