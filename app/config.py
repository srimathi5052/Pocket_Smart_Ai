import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
STATIC_DIR = BASE_DIR / "app" / "static"
TEMPLATES_DIR = BASE_DIR / "app" / "templates"


def _load_dotenv():
    env_file = BASE_DIR / ".env"
    if not env_file.exists():
        return

    for line in env_file.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or "=" not in stripped:
            continue
        key, value = stripped.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip())


_load_dotenv()


class Settings:
    def __init__(self):
        self.secret_key = os.getenv("SECRET_KEY", "dev-secret-key")
        self.gemini_api_key = (
            os.getenv("GEMINI_API_KEY")
            or os.getenv("Gemini_Api_key")
            or ""
        )
        self.gemini_model = os.getenv("GEMINI_MODEL", "gemini-2.0-flash")


settings = Settings()
