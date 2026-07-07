# EmpowerNet AI — Architecture Overview

## System Architecture

EmpowerNet AI is a monorepo containing three primary components:

| Component | Path | Runtime |
|-----------|------|---------|
| FastAPI Backend | `backend/` | Python 3.10+, Uvicorn |
| React Frontend | `frontend/` | Node 18+, Vite |
| Chrome Extension | `empowernet-extension/` | Chrome Manifest V3 |

---

## Backend Layer

### Entry Point

`backend/main.py` creates the FastAPI application, registers modular routers, and configures middleware.

```
main.py
├── CORSMiddleware (allow_origins=[*])
├── Request logging middleware
├── GET  /          → health root
├── GET  /health    → health check
├── POST /api/scan          [scan.router]
├── POST /api/verify        [scan.router]
├── POST /realtime/video    [realtime.router]
├── POST /realtime/audio    [realtime.router]
├── POST /analyze/text      [scan.router]
├── POST /analyze/image     [scan.router]
├── POST /analyze/video     [scan.router]
├── POST /analyze/audio     [scan.router]
└── WS   /ws/dashboard      [websocket.router]
```

### Configuration

`backend/config/config.py` exposes a `Settings` singleton that loads all environment variables. All services read from `settings` — no service calls `os.getenv()` directly.

### ML Inference Pipelines

Each modality has a dedicated inference module in `backend/ml/`:

| Module | Description |
|--------|-------------|
| `text_infer.py` | Transformer-based scam/phishing/propaganda classifier |
| `image_infer.py` | ELA + vision ensemble deepfake detector |
| `audio_infer.py` | MFCC + F0 + optional Whisper STT voice clone detector |
| `video_plus_infer.py` | 5-point frame sampler + FFmpeg audio extraction |
| `ml_service.py` | Vision ensemble singleton; real-time video/audio processor |
| `child_safety.py` | NSFW + cyberbullying content filter |
| `explain.py` | Explainability: human-readable verdict builder |

**Execution modes:**

- `LOAD_MODELS=false` (default): Uses Gemini Flash for vision tasks, heuristic signals for audio
- `LOAD_MODELS=true`: Loads local HuggingFace models (requires GPU recommended)

### Evidence Ledger

`backend/blockchain/blockchain_service.py` implements the `BlockchainService` singleton:

```
scan result
    │
    ▼
SHA-256(category + riskScore + confidence + explanation[:3])
    │
    ▼
BlockchainService.anchor_evidence(hash, category)
    │
    ├── [PRIVATE_KEY set] → web3.py → Polygon Amoy transaction → real tx hash
    │
    └── [default]         → secrets.token_hex(32) simulation → persisted to
                            backend/blockchain/simulated_blockchain.json
```

> **Important:** In local simulation mode, transaction hashes are cryptographically random strings that look like valid Polygon hashes but are **not** verifiable on-chain. The system is fully architected for live anchoring — only credentials are missing.

---

## Frontend Layer

The React frontend in `frontend/` is a Vite + TypeScript SPA using Tailwind CSS for styling and Zustand for global state.

### Page Map

| Page | Route | Description |
|------|-------|-------------|
| Landing | `/` | Marketing/info page |
| Dashboard | `/dashboard` | Scan history and stats |
| Scan | `/scan` | Multi-modal scan input |
| Evidence Log | `/evidence` | Forensic hash table + certificates |
| Reports | `/reports` | PDF generation + authority submission |
| Threat Intelligence | `/threats` | Aggregated threat feed |
| Meeting Shield | `/meeting` | Real-time video call protection |
| Social Scanner | `/social` | Social media content analysis |

### API Client

`frontend/services/api.ts` is the single API gateway. It reads `VITE_API_URL` from the environment to determine the backend base URL.

---

## Chrome Extension

The extension (`empowernet-extension/`) follows Manifest V3 architecture:

```
background.js     — Service worker: auto-scans page content
content.js        — Injected into pages: extracts text, detects scams inline
popup.html/js     — Extension popup with live/history/media tabs
media_scanner.js  — Scans images/videos embedded in pages
meeting_content.js — Hooks into Google Meet / Zoom for real-time frame capture
child_safety.js   — Child safety content hider
offscreen.js      — Offscreen document for audio capture
```

---

## Data Flow: Full Scan Request

```
User (Browser or Extension)
    │
    │  POST /api/scan  { type, content, label }
    ▼
FastAPI (scan.router)
    │
    ├── Route to inference pipeline (text/image/audio/video)
    │       │
    │       ▼
    │   ML pipeline returns { category, confidence, riskScore, explanation, ... }
    │
    ├── generate_scan_hash(result)  →  SHA-256 evidence hash
    │
    ├── blockchain_service.anchor_evidence(hash, category)
    │       │
    │       └── Returns tx_hash (real or simulated)
    │
    └── Return ScanResponse {
            category, confidence, riskScore,
            explanation, modelDetails, userSummary,
            evidenceHash, blockchain { network, transactionHash, ... }
        }
```

---

## Deployment

### Backend (Railway / Docker)

The `Dockerfile` builds the Python backend. `railway.json` configures the start command.

```dockerfile
# Key environment variables to set on Railway:
PORT=8001
LOAD_MODELS=false
GEMINI_API_KEY=<your_key>
# Optional (enables live blockchain):
PRIVATE_KEY=<polygon_wallet_key>
CONTRACT_ADDRESS=<deployed_contract>
```

### Frontend (Vercel)

The frontend is deployed from `frontend/` with Vite as the build tool. `vercel.json` in `frontend/` configures routing SPA rewrites.

```bash
# Build command
npm run build

# Output directory
dist/

# Environment variable on Vercel:
VITE_API_URL=https://your-railway-backend.up.railway.app
```
