# Contributing to EmpowerNet AI

Thank you for your interest in contributing to EmpowerNet AI. This document provides guidelines for contributing to the project.

---

## Code of Conduct

By participating in this project, you agree to uphold a respectful and inclusive environment. Harassment, discrimination, and abusive behavior will not be tolerated.

---

## How to Contribute

### Reporting Issues

Before opening a new issue, please search existing issues to avoid duplicates.

When reporting a bug, include:
- A clear, descriptive title
- Steps to reproduce the problem
- Expected vs. actual behavior
- Environment details (OS, Python version, Node version, browser)
- Relevant logs or screenshots

### Suggesting Enhancements

Open a GitHub Issue with the label `enhancement`. Describe:
- The problem your suggestion solves
- A proposed solution or design
- Any alternatives you've considered

---

## Development Setup

### Prerequisites

| Tool | Version |
|------|---------|
| Python | ≥ 3.10 |
| Node.js | ≥ 18.x |
| Git | Latest |

### Local Installation

```bash
# 1. Clone the repo
git clone https://github.com/aayushijohri/EmpowerNet-AI.git
cd EmpowerNet-AI

# 2. Set up the Python backend
cd backend
pip install -r requirements.txt
cp ../.env.example ../.env   # Fill in required values

# 3. Start the backend
uvicorn main:app --reload --port 8001

# 4. Set up the frontend (in a new terminal)
cd frontend
npm install
npm run dev
```

---

## Pull Request Process

1. **Fork** the repository and create your branch from `main`:
   ```bash
   git checkout -b feat/your-feature-name
   ```

2. **Write clean, typed code.** Follow the existing patterns:
   - Backend: type hints and docstrings on all public functions
   - Frontend: TypeScript strict mode, functional components only

3. **Test your changes** before submitting.

4. **Write a clear commit message** following [Conventional Commits](https://www.conventionalcommits.org/):
   ```
   feat: add audio deepfake detection via Whisper
   fix: resolve race condition in video frame sampler
   docs: update blockchain simulation architecture notes
   ```

5. **Open a Pull Request** against `main` and fill in the PR template.

6. Ensure your PR:
   - Does not break existing API contracts
   - Does not remove existing functionality without discussion
   - Includes relevant documentation updates

---

## Code Style

### Python (Backend)

- Follow [PEP 8](https://peps.python.org/pep-0008/)
- Use type hints on all function signatures
- Add docstrings to public functions and classes
- Use `logging` instead of bare `print()` calls

```python
# Good
def analyze_audio(base64_audio: str) -> dict:
    """
    Analyze an audio clip for voice cloning and scam content.

    Args:
        base64_audio: Base64-encoded audio bytes.

    Returns:
        A dict with category, confidence, riskScore, and explanation.
    """
```

### TypeScript (Frontend)

- Use explicit return types on functions where the type is not obvious
- Prefer named exports
- Avoid `any` — use `unknown` with narrowing where needed

---

## Project Structure

```
EmpowerNet-AI/
├── backend/
│   ├── api/routers/    # Modular FastAPI route handlers
│   ├── blockchain/     # Evidence logging service (simulation-ready)
│   ├── config/         # Centralized settings
│   ├── ml/             # Inference pipelines per modality
│   ├── models/         # Pydantic request/response schemas
│   └── main.py         # Application entrypoint
├── frontend/
│   ├── pages/          # React page components
│   ├── services/       # API client layer
│   └── store/          # Zustand global state
├── empowernet-extension/  # Chrome Extension (Manifest V3)
└── docs/               # Architecture diagrams and documentation
```

---

## Blockchain / Evidence Ledger

The blockchain anchoring system currently runs in **local simulation mode**. It generates a deterministic SHA-256 hash for every scan result and stores it in a persistent JSON file. When `PRIVATE_KEY` and `CONTRACT_ADDRESS` are provided, the service upgrades to live Polygon Amoy transactions automatically.

Contributors should **not** overstate the current state of this feature in documentation or UI copy. Use phrasing like:
- ✅ "Evidence logging (Polygon Amoy-ready, currently in local simulation mode)"
- ❌ "Anchored on the Polygon blockchain"

---

## License

By contributing to EmpowerNet AI, you agree that your contributions will be licensed under the [MIT License](LICENSE).
