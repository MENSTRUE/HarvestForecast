# Deployment and operational readiness

**Current status:** locally demonstrated research prototype. The user provided a screenshot showing model status online, but no submitted prediction outcome, automated integration test or public deployment URL is independently verified. The GitHub source does not contain infrastructure-as-code, CI deployment or authentication.

From the repository root in PowerShell: `& "C:\DevEnvs\ai-general\Scripts\python.exe" -m pip install -r backend\requirements.txt` then `& "C:\DevEnvs\ai-general\Scripts\python.exe" -m uvicorn backend.app.main:app --reload --port 8000`; in another terminal: `cd frontend; npm install; npm run dev`. Use `http://127.0.0.1:8000/docs` and `http://127.0.0.1:5173`. Before public deployment: pin/scan dependencies, disable debug reload, add auth/rate limits/logging/monitoring, establish supported input categories, external validation, operational data availability and licensing.


## Evidence / Bukti

- [Experiment notebook](../../notebooks/harvestforecast.ipynb)
- [Experiment metrics](../../reports/extracted/heldout_test_metrics.json)
- [Run configuration](../../reports/extracted/run_config.json)
- [Source inventory](../../reports/extracted/dataset_inventory.csv)
- [Limitations](limitations.md)
