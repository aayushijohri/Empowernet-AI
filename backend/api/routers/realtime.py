import logging
from fastapi import APIRouter, HTTPException
from ml.ml_service import ml_service
from models.schemas import (
    RealtimeVideoRequest, RealtimeVideoResponse,
    RealtimeAudioRequest, RealtimeAudioResponse
)

logger = logging.getLogger("empowernet.realtime_router")
router = APIRouter()

@router.post(
    "/realtime/video",
    response_model=RealtimeVideoResponse,
    tags=["Realtime"],
    summary="Analyze a single video frame for deepfake risk (Meeting Shield)",
)
async def realtime_video(payload: RealtimeVideoRequest):
    participant_id = payload.participant_id
    frame_b64 = payload.frame
    
    try:
        result = await ml_service.process_video_frame(participant_id, frame_b64)
        return result
    except Exception as e:
        logger.exception("Error in /realtime/video")
        raise HTTPException(status_code=500, detail=str(e))

@router.post(
    "/realtime/audio",
    response_model=RealtimeAudioResponse,
    tags=["Realtime"],
    summary="Analyze an audio chunk for voice cloning risk (Meeting Shield)",
)
async def realtime_audio(payload: RealtimeAudioRequest):
    participant_id = payload.participant_id
    audio_b64 = payload.audio
    
    try:
        result = await ml_service.process_audio_chunk(participant_id, audio_b64)
        return result
    except Exception as e:
        logger.exception("Error in /realtime/audio")
        raise HTTPException(status_code=500, detail=str(e))
