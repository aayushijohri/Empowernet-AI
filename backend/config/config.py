import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Settings:
    # API Settings
    PORT: int = int(os.getenv("PORT", 8001))
    HOST: str = "0.0.0.0"
    
    # ML Settings
    LOAD_MODELS: bool = os.getenv("LOAD_MODELS", "false").lower() == "true"
    GEMINI_API_KEY: str | None = os.getenv("GEMINI_API_KEY") or os.getenv("API_KEY")
    
    # Blockchain Settings
    POLYGON_RPC_URL: str = os.getenv("POLYGON_RPC_URL", "https://rpc-amoy.polygon.technology/")
    PRIVATE_KEY: str | None = os.getenv("PRIVATE_KEY")
    CONTRACT_ADDRESS: str | None = os.getenv("CONTRACT_ADDRESS")
    
    # Mode Summary
    @property
    def is_blockchain_simulated(self) -> bool:
        return not bool(self.PRIVATE_KEY and self.CONTRACT_ADDRESS)

settings = Settings()
