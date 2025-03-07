# App settings

import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

class Config:
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./projects.db")
    DEBUG = os.getenv("DEBUG", "True").lower() in ("true", "1", "yes")

config = Config()

