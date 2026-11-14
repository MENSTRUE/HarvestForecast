# Backend — FastAPI inference service

## Architecture

[`app/main.py`](app/main.py) is the current API. `GET /api/v1/health` reports local model availability, `GET /api/v1/model` returns model metadata and saved test metrics, and `POST /api/v1/predict` runs regression. No auth, persistent database, background scheduler or production logging framework is implemented.

## Request contract

```json
{"area":"India","item":"Rice, paddy","year":2010,"average_rain_fall_mm_per_year":1200,"pesticides_tonnes":50000,"avg_temp":25}
```

The JSON above is an illustrative API payload, **not a validated sample from the training data or an observed model result**. Exactly six properties are accepted; strings are required for area/item. Pydantic constrains `year` to 1900–2100, rainfall to 0–30000, pesticides to 0–100000000, and temperature to -80–70. These are software validation bounds, **not agronomic validity bounds**. Invalid requests return 422.

## Loader and response

`joblib.load` reads the **trusted local dictionary** whose `kind` must be `sklearn_pipeline`. The implementation extracts `artifact['model']`, checks feature order, `target=value_hg_ha` and `unit=hg/ha`; the pipeline includes its training-fitted encoder and imputer. Output keys are `prediction_hg_ha`, `prediction_kg_ha`, `prediction_tonnes_ha`, `unit`, `model`, `disclaimer`. Conversions are 1 hg = 0.1 kg and 1 hg = 0.0001 tonne.

## Setup / tests

From repository root:

```powershell
& "C:\DevEnvs\ai-general\Scripts\python.exe" -m pip install -r backend\requirements.txt
& "C:\DevEnvs\ai-general\Scripts\python.exe" -m uvicorn backend.app.main:app --reload --port 8000
```

Check `/api/v1/health` and `/docs`; verify a prediction on known, historical inputs and inspect actual JSON. An automated test suite is not present in the audited GitHub tree.

## Security and limitations

Only load an artifact you trained or audited: joblib/pickle can execute arbitrary code. CORS is limited to local Vite origins, but that is **not authentication**. The encoder ignores unknown categorical labels; lack of an error does not establish in-distribution validity. For public hosting implement auth, rate limits, input controls, dependency review and operational monitoring. See [architecture](../docs/en/architecture.md) and [limitations](../docs/en/limitations.md).
