# dev-find
A minimal Flask service that fetches developer job listings from RemoteOK.

## Quick start
1. Install dependencies:
```bash
pip install -r requirement.txt
```
2. Run the app:
```bash
python3 app.py
```

## Endpoints
- `/api/jobs?n=<number>` — returns up to `<number>` jobs with position and tags
- `/api/skills` — returns skill counts aggregated from job tags

## Notes
- Uses RemoteOK API: `https://remoteok.com/api`
- Logs are written to `info.log`
