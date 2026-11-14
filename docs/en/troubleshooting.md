# Troubleshooting and verification

**Model unavailable:** first verify `models/harvestforecast_champion.joblib` exists; this file is a **dictionary**, not directly a sklearn estimator. Inspect `artifact["kind"] == "sklearn_pipeline"`, `artifact["model"]`, its `feature_names_in_`, target and unit. Earlier loader code expecting a bare estimator was incompatible; the checked `backend/app/main.py` now extracts the nested model.

**API disconnected:** run Uvicorn on port 8000; Vite proxies `/api`. **HTTP 422:** check flat JSON, numeric bounds, exact six keys, and whether category values follow training naming. **Non-finite or suspicious prediction:** compare data cleaning/preprocessing and unit conversions, and test with historical rows whose true inputs are available. **Build issues:** `cd frontend; npm install; npm run build`. Never unpickle an untrusted downloaded artifact.


## Evidence / Bukti

- [Experiment notebook](../../notebooks/harvestforecast.ipynb)
- [Experiment metrics](../../reports/extracted/heldout_test_metrics.json)
- [Run configuration](../../reports/extracted/run_config.json)
- [Source inventory](../../reports/extracted/dataset_inventory.csv)
- [Limitations](limitations.md)
