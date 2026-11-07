# Architecture

## High-level flow
1. Browser sends an upload, a supported public media URL, or a cloud-object reference to the API.
2. API validates source type, size policy, and ownership metadata, then creates a job record (persistent job storage arrives in a later phase).
3. A dispatcher selects a local worker or configured cloud worker.
4. Worker stages media in private temporary storage, probes it, and runs transcription/highlight/render tasks.
5. Outputs are stored privately and exposed through short-lived authorized links in later phases.

## Boundaries
- `SourceAdapter`: normalizes upload, URL, and cloud-object inputs.
- `ProcessingProvider`: common interface for local and cloud execution.
- `LocalProcessingProvider`: local FFmpeg capability check and future task runner.
- `CloudProcessingProvider`: explicit unconfigured placeholder; never silently uploads user media.
- API owns validation and orchestration; workers own expensive CPU/GPU tasks.

## Local vs cloud
Local mode keeps media on the user's machine/server and avoids per-minute cloud costs, but uses available CPU/GPU/RAM. Cloud mode is opt-in and requires a configured provider, storage policy, credentials, and cost limits. The initial implementation defaults to local development and reports cloud as unconfigured.

## Windows developer profile
A 16 GB RAM / RTX 3050 6 GB machine can develop and test the control plane. Heavy transcription/rendering should use small models, bounded concurrency, and temporary-file cleanup. GPU acceleration is optional; CPU fallback must remain available.

## Security requirements before production
- Authentication and per-user authorization.
- Upload size/type limits, malware scanning, isolated media processing.
- SSRF defenses for URL ingestion (allowlist schemes, block private/link-local IP ranges, re-check redirects and DNS).
- Signed object URLs and private buckets for cloud storage.
- Job quotas, timeouts, rate limits, audit logs, retention/deletion controls.
- Never execute arbitrary user-supplied URLs or commands through a shell.
