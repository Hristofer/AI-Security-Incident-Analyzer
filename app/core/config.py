import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    def __init__(self):
        self.app_name = "AI Security Incident Analyzer"
        self.version = "1.0.0"

        self.database_url = os.getenv(
            "DATABASE_URL",
            "sqlite:///incident_analyzer.db",
        )

        self.anthropic_api_key = os.getenv("ANTHROPIC_API_KEY", "")
        self.openai_api_key = os.getenv("OPENAI_API_KEY", "")

        self.log_level = os.getenv("LOG_LEVEL", "INFO")


settings = Settings()
