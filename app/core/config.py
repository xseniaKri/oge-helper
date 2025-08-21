from pydantic_settings import BaseSettings
from pydantic import BaseModel
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
ENV_PATH = BASE_DIR.parent / ".env"

class AuthJWT(BaseModel):
    private_key_path: Path = BASE_DIR / "certs" / "jwt-private.pem"
    public_key_path: Path = BASE_DIR / "certs" / "jwt-public.pem"
    algorithm: str = "RS256"

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/ogehelp"

    APP_NAME: str = "Oge Helper"
    APP_VERSION: str = "0.1.0"
    DEBUG: bool = True

    auth_jwt: AuthJWT = AuthJWT()

    class Config:
        env_file = ENV_PATH
        env_file_encoding = "utf-8"

settings = Settings()