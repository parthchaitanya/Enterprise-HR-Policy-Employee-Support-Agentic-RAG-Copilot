from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path 

BASE_DIR = Path(__file__).resolve().parents[2]

class Settings(BaseSettings):
    app_name: str = "Enterprise HR Policy Employee Support Agentic RAG Copilot"
    app_env: str = "development"
    groq_api_key: str = ""
    groq_model: str = "openai/gpt-oss-120b"
    tavily_api_key: str = ""
    pinecone_api_key: str = ""
    pinecone_index_name: str = "enterprise-hr-policy-agentic-rag-copilot"
    pinecone_namespace: str = "company-it-kit"
    embedding_model: str = "sentence-transformers/all-MiniLM-L6-v2"
    top_k: int = 4
    max_retries: int = 1
    admin_api_key: str = "change-me"
    audit_db_path: str = str(BASE_DIR / "data" / "audit.db")
    uploads_dir: str = str(BASE_DIR / "uploads")
    sample_kb_dir: str = str(BASE_DIR / "data" / "sample_kb")

    model_config = SettingsConfigDict(env_file=str(BASE_DIR / ".env"), extra="ignore")



@lru_cache()
def get_settings() -> Settings:
    return Settings()