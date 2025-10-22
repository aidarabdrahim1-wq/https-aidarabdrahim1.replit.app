# Backend

Run locally:

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

API:
- GET `/api/v1/health/health` — health check
- POST `/api/v1/students/` — create student
- GET `/api/v1/students/` — list students
- GET `/api/v1/students/{id}` — get student
- PATCH `/api/v1/students/{id}` — update student
- POST `/api/v1/explain/` — explain topic
- POST `/api/v1/tests/generate` — generate test
- POST `/api/v1/tests/grade` — grade answers
- POST `/api/v1/agent/solve` — agent solve (MVP=explain)
