from pydantic_settings import BaseSettings

class settings(BaseSettings):
    APP_NAME: str = "ENTERPRISE_MULTIMODEL_GENAI_PLATFORM"
    APP_VERSION: str = "0.1.0"
    ENVIRONMENT: str = "development"
    DEBUG: bool = "True"

    class config:
        env_file = ".env"

settings = settings()            