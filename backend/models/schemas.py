from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any

# --- API Scan Input/Output Schemas ---

class ScanRequest(BaseModel):
    type: str = Field(..., description="Content type to analyze: text, image, audio, or video")
    content: str = Field(..., description="Base64 encoded content or raw text")
    label: Optional[str] = Field(default="Unknown Source", description="Source identifier/label")


class BlockchainInfo(BaseModel):
    network: str = Field(..., description="Polygon Amoy (Simulated)")
    type: str = Field(..., description="Smart Contract (EVM)")
    transactionHash: str = Field(..., description="Transaction hash or simulation hash")
    explorerUrl: str = Field(..., description="Blockchain block explorer link")
    status: str = Field(..., description="confirmed")


class ModelDetails(BaseModel):
    architecture: str
    featuresAnalysed: List[str]


class UserSummary(BaseModel):
    verdict: str
    reason: str
    triggers: Optional[List[str]] = None


class ScanResponse(BaseModel):
    category: str
    confidence: float
    riskScore: int
    explanation: List[str]
    modelDetails: ModelDetails
    userSummary: UserSummary
    evidenceHash: str
    blockchain: BlockchainInfo


# --- Verification Schemas ---

class VerifyRequest(BaseModel):
    evidenceHash: str = Field(..., description="Forensic proof hash to verify")


class VerifyResponse(BaseModel):
    status: str
    blockchain: Dict[str, Any]


# --- Realtime API Schemas ---

class RealtimeVideoRequest(BaseModel):
    participant_id: str = Field(default="default")
    frame: str = Field(..., description="Base64 image frame")
    timestamp: Optional[int] = Field(default=None)


class RealtimeVideoResponse(BaseModel):
    participant_id: str
    deepfake: float
    liveness: float
    status: str
    raw_deepfake: float
    temporal_anomaly: bool


class RealtimeAudioRequest(BaseModel):
    participant_id: str = Field(default="default")
    audio: str = Field(..., description="Base64 audio chunk")


class RealtimeAudioResponse(BaseModel):
    voice_authenticity: float
    voice_status: str


# --- Social Media Analytics Schemas ---

class SyntheticMediaRequest(BaseModel):
    image: str = Field(..., description="Base64 image string")


class AnalyzeTextRequest(BaseModel):
    text: str = Field(..., description="Text content to score")


class AnalyzeTextResponse(BaseModel):
    category: str
    confidence: float
    riskScore: int
    toxicity_score: float
    safety_flags: List[str]
    is_safe_for_children: bool
    intent_label: str


class AnalyzeImageRequest(BaseModel):
    image: Optional[str] = Field(default=None, description="Base64 image")
    image_url: Optional[str] = Field(default=None, description="Image URL descriptor")


class AnalyzeImageResponse(BaseModel):
    deepfake_probability: float
    verdict: str
    is_safe_for_children: bool
    safety_flags: List[str]
    vision_ensemble: float
    texture_score: float


class AnalyzeMediaRequest(BaseModel):
    video: Optional[str] = Field(default=None, description="Base64 video content")
    video_url: Optional[str] = Field(default=None)
    audio: Optional[str] = Field(default=None, description="Base64 audio content")
    audio_url: Optional[str] = Field(default=None)
