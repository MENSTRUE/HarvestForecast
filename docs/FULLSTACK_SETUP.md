# HarvestForecast Full-Stack — Day 37

This package adds `backend/`, `frontend/` and `scripts/` only. It does not replace the trained model, notebook, existing README or dataset reports.

## Backend

```powershell
cd "D:\porto\100 day\day 37"
& "C:\DevEnvs\ai-general\Scripts\python.exe" -m pip install -r backend\requirements.txt
& "C:\DevEnvs\ai-general\Scripts\python.exe" -m uvicorn backend.app.main:app --reload --port 8000
```

API docs: http://127.0.0.1:8000/docs

## Frontend

```powershell
cd "D:\porto\100 day\day 37\frontend"
npm install
npm run dev
```

Dashboard: http://127.0.0.1:5173

## Important

The model requires exactly: `area`, `item`, `year`, `average_rain_fall_mm_per_year`, `pesticides_tonnes`, `avg_temp`. The app validates model `feature_names_in_` before inference. The UI does not guess area/crop categories or fabricate values. Supply exact category spellings from the training dataset. This is retrospective benchmarking, not a pre-season yield advisory system. Do not unpickle untrusted model files.
