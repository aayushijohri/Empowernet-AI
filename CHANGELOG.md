# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

---

## [Unreleased]

### Added
- `backend/config/config.py` — Centralized settings loader using environment variables
- `backend/models/schemas.py` — Strict Pydantic request/response schemas for all API endpoints
- `backend/api/routers/scan.py` — Modular FastAPI router for scan and verification endpoints
- `backend/api/routers/realtime.py` — Modular router for real-time video/audio analysis
- `backend/api/routers/websocket.py` — WebSocket connection manager with proper error handling
- `CONTRIBUTING.md` — Contributor guidelines, setup instructions, and code style rules
- `SECURITY.md` — Vulnerability reporting process and security disclosures
- `CHANGELOG.md` — This file
- `frontend/vite-env.d.ts` — Extended Vite env type declarations (`DEV`, `PROD`, `MODE`)

### Changed
- `backend/main.py` — Refactored to use modular routers, centralized settings, and structured logging
- `backend/blockchain/blockchain_service.py` — Now reads config from `settings` instead of raw `os.getenv`
- `frontend/pages/EvidenceLog.tsx` — Tempered blockchain claims to reflect local simulation mode
- `frontend/pages/Reports.tsx` — Updated PDF and preview copy to reflect evidence ledger simulation mode
- `frontend/pages/ScanPage.tsx` — Updated blockchain panel description to reflect simulation mode

### Removed
- `BLOCKCHAIN_INTEGRATION_GUIDE.md` — Empty file, removed during repository audit
- `backend/utils/preprocessing.py` — Empty placeholder file removed
- Stale temporary audio/video files (`temp_audio_*.tmp`, `temp_video.mp4`) removed from repository

### Fixed
- Duplicate `return result` statement in original `main.py` (line 297)
- `BlockchainService` no longer imports `dotenv` directly — configuration is centralized

---

## [1.0.0] — 2025-06 (Initial Hackathon Release)

### Added
- Multi-modal scan endpoint (`/api/scan`) supporting text, image, audio, and video
- Chrome Extension (Manifest V3) with real-time page protection and popup UI
- FastAPI backend with ML inference pipelines:
  - Text: scam/phishing/propaganda detection via fine-tuned transformer
  - Image: ELA + vision ensemble (EfficientNet-B5, ViT, Organika/sdxl-detector)
  - Audio: MFCC heuristics + optional `motheecreator/Deepfake-audio-detection`
  - Video: 5-point frame sampling + audio extraction via FFmpeg
- React frontend (Vite + Tailwind + Zustand) with:
  - Scan Page, Evidence Log, Reports Page, Threat Intelligence, Meeting Shield, Social Scanner
- Blockchain evidence logging (Polygon Amoy-ready, runs in simulation mode by default)
- SHA-256 forensic proof hashing for every scan result
- PDF forensic report generator with `jsPDF`
- Child safety content filter (text and image)
- Deployment configs for Railway (`railway.json`) and Vercel (`vercel.json`)
