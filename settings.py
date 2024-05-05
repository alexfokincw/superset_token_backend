import os
from dotenv import load_dotenv

if os.path.exists(".env"):
    print("load .env")
    load_dotenv()

SUPERSET_BASE_URL = os.environ.get("SUPERSET_BASE_URL", "")

SUPERSET_USER = os.environ.get("SUPERSET_USER", "")

SUPERSET_FIRST_NAME = os.environ.get("SUPERSET_FIRST_NAME", "")

SUPERSET_LAST_NAME = os.environ.get("SUPERSET_LAST_NAME", "")

SUPERSET_PASSWORD = os.environ.get("SUPERSET_PASSWORD", "")

FRONTEND_BASE_URL = os.environ.get("FRONTEND_BASE_URL", "")
