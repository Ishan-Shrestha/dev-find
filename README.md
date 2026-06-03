# dev-find
A minimal Flask service that fetches developer job listings from RemoteOK and exposes a small REST API for jobs, skill counts, and search.

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
- `/` — renders the front-end page from `templates/index.html`.
- `/api/jobs?n=<number>` — returns up to `<number>` jobs with `position` and `tags` (default `10`).
- `/api/skills` — returns aggregated skill counts from job tags.
- `/api/jobs/search?query=<query>` — returns jobs whose position or tags exactly match `<query>` (case-insensitive).

## Notes
- The service fetches data from the RemoteOK API at `https://remoteok.com/api`.
- Application logs are written to `info.log`.
- Search uses exact matches on position or tag values, not substring matching.

## File hierarchy

- `app.py` — Flask application with API routes and HTML rendering.
- `fetch.py` — fetches and parses data from RemoteOK.
- `requirement.txt` — Python dependencies.
- `README.md` — project documentation.
- `templates/index.html` — front-end page rendered by the root route.
