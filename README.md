# ClipForge AI

AI-assisted video repurposing workspace. Phase 1 establishes the web/API foundation and processing boundaries.

## Architecture
- `frontend/`: Next.js App Router + TypeScript dashboard.
- `backend/`: FastAPI service, health endpoint, typed ingestion contracts.
- Local processing: FFmpeg adapter (optional system binary) and worker boundary.
- Cloud processing: provider-neutral adapter interface; no cloud provider or paid API is enabled by default.
- Storage: local development storage; cloud storage adapters are added only after credentials and provider choice.

## Prerequisites
- Node.js 20.9+ and npm
- Python 3.11+
- FFmpeg installed and available on PATH (optional for the Phase 1 health check)

## Run locally
### API
```powershell
cd backend
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
Copy-Item .env.example .env
uvicorn app.main:app --reload --port 8000
```

### Web
In another terminal:
```powershell
cd frontend
npm install
Copy-Item .env.example .env.local
npm run dev
```
Open http://localhost:3000. API health: http://localhost:8000/api/v1/health.

## Phase 1 scope
- Working frontend shell and API health endpoint.
- Upload/URL/cloud-storage ingestion contracts and validation boundary.
- Local/cloud processing interfaces, not yet a production transcoding pipeline.
- No authentication, paid integrations, public deployment, or social publishing in this phase.

## Safety and constraints
Only process videos you own or are authorized to use. URL ingestion must respect platform terms and access controls; do not bypass DRM, login walls, or download restrictions. Never commit API keys, cookies, or private media. Large media files are excluded from Git.

## Project status
Phase 1 foundation. See `docs/ARCHITECTURE.md` and `docs/PHASE-1.md`.
