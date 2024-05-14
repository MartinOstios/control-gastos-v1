import os
from dotenv import load_dotenv

load_dotenv()
auth_secret_key = os.getenv("AUTH_SECRET_KEY")
auth_algorithm = os.getenv("AUTH_ALGORITHM")
