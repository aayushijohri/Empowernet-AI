# Security Policy

## Supported Versions

| Version | Supported |
|---------|-----------|
| Latest (`main`) | ✅ Active |
| Older branches | ❌ Not supported |

---

## Reporting a Vulnerability

**Please do not open public GitHub Issues for security vulnerabilities.**

If you discover a security issue, please report it responsibly by emailing:

📧 **aayushijohri@example.com** *(replace with your contact)*

Include in your report:
- A clear description of the vulnerability
- Steps to reproduce
- Potential impact assessment
- Any suggested mitigations

We will acknowledge your report within **48 hours** and provide a status update within **7 days**.

---

## Security Considerations

### API Security

- The backend CORS policy is currently set to `allow_origins=["*"]` for development convenience. In production, this should be restricted to your specific frontend domain.
- No authentication is implemented in the current version. Adding an API key or JWT middleware is recommended before production deployment.

### Blockchain / Evidence Ledger

- The system operates in **local simulation mode** by default. The simulated transaction hashes are cryptographically random but are **not** verifiable on any real blockchain network unless `PRIVATE_KEY` and `CONTRACT_ADDRESS` env vars are supplied.
- Do **not** commit real private keys to the repository. Always use `.env` files excluded by `.gitignore`.

### Environment Variables

Sensitive configuration is managed via environment variables. See `.env.example` for required keys. Never commit a populated `.env` file.

```bash
# Required for live blockchain (optional; simulation mode is default)
PRIVATE_KEY=your_polygon_wallet_private_key
CONTRACT_ADDRESS=your_deployed_contract_address

# Required for cloud ML inference
GEMINI_API_KEY=your_gemini_key
```

### ML Model Inputs

All user-supplied content (text, base64 images, audio, video) is processed locally using inference pipelines. No user data is sent to external services unless `GEMINI_API_KEY` is configured and `LOAD_MODELS=false`.

---

## Out of Scope

The following are currently **not** in scope for security bounty or priority fixes:
- CORS policy in development mode
- Missing rate limiting (noted as a known gap)
- Chrome Extension content script permissions (uses standard Manifest V3 permissions)
