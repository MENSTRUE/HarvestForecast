# Architecture and API contracts

The local React 18 + TypeScript + Vite 6 frontend calls a same-origin `/api` path proxied by Vite to FastAPI on `127.0.0.1:8000`. No database, user authentication or remote sensor integration is present in the checked source. The frontend contains Overview, Yield prediction and Model insights views; these are client-side state views, not separate URL routes.

FastAPI exposes `GET /api/v1/health`, `GET /api/v1/model` and `POST /api/v1/predict`. Prediction accepts a flat JSON object with six exact keys (`area`, `item`, `year`, `average_rain_fall_mm_per_year`, `pesticides_tonnes`, `avg_temp`). It validates values via Pydantic, constructs a DataFrame in canonical order, runs the nested trusted `artifact["model"]` sklearn pipeline and returns `prediction_hg_ha`, `prediction_kg_ha`, `prediction_tonnes_ha`, plus a disclaimer. Model loading is cached via `lru_cache`. CORS is restricted to local Vite origins.


## Evidence / Bukti

- [Experiment notebook](../../notebooks/harvestforecast.ipynb)
- [Experiment metrics](../../reports/extracted/heldout_test_metrics.json)
- [Run configuration](../../reports/extracted/run_config.json)
- [Source inventory](../../reports/extracted/dataset_inventory.csv)
- [Limitations](limitations.md)
