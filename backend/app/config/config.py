# app/config/config.py
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://threat_user:changeme@localhost/threat_db")
JWT_SECRET = os.getenv("JWT_SECRET", "your_jwt_secret")
DEBUG = os.getenv("DEBUG", "True") == "True"
