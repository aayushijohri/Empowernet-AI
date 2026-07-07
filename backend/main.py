import logging
import os
import uvicorn
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from config.config import settings
from api.routers import scan, realtime, websocket

# Configure Central Logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger("empowernet")

app = FastAPI(
    title="EmpowerNet AI Backend API",
    description="Production-ready core API for multi-modal AI scam, deepfake detection, and cryptographic evidence logging.",
    version="1.1.0",
    openapi_tags=[
        {"name": "System", "description": "Health checks and API status"},
        {"name": "Analysis", "description": "Multi-modal forensic analysis endpoints (text, image, audio, video)"},
        {"name": "Evidence", "description": "Cryptographic proof hash verification against the evidence ledger"},
        {"name": "Realtime", "description": "Frame-by-frame and audio-chunk analysis for live meeting protection"},
    ]
)

# Global CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request logger middleware
@app.middleware("http")
async def log_requests(request: Request, call_next):
    if "/realtime/" in request.url.path or "/detect/" in request.url.path:
        logger.info(f"Incoming Request: {request.method} {request.url.path}")
    response = await call_next(request)
    return response

# Root endpoints
@app.get("/", tags=["System"], summary="API status check")
def read_root():
    return {"status": "EmpowerNet API is Online"}

@app.get("/health", tags=["System"], summary="Health probe for deployment platforms")
def health_check():
    return {"status": "healthy"}

# Register Modular Routers
app.include_router(scan.router)
app.include_router(realtime.router)
app.include_router(websocket.router)

if __name__ == "__main__":
    # Get port from environment or settings
    port = int(os.getenv("PORT", settings.PORT))
    logger.info(f"Starting EmpowerNet Backend API on port {port}")
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=port,
        timeout_keep_alive=30,
        reload=False
    )
