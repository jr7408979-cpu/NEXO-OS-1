import os


APP_NAME = os.getenv("NEXO_APP_NAME", "NEXO OS")
ENVIRONMENT = os.getenv("NEXO_ENV", "development")
DEBUG = os.getenv("NEXO_DEBUG", "true").lower() == "true"
