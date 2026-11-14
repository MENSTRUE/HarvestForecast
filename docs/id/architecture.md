# Arsitektur dan kontrak API

Frontend lokal React 18 + TypeScript + Vite 6 memanggil path `/api` same-origin yang diproxy Vite ke FastAPI pada `127.0.0.1:8000`. Kode yang diperiksa belum punya database, autentikasi pengguna, atau integrasi sensor jarak jauh. Frontend punya tampilan Overview, Yield prediction, dan Model insights; ini state client-side, bukan URL route terpisah.

FastAPI menyediakan `GET /api/v1/health`, `GET /api/v1/model`, dan `POST /api/v1/predict`. Prediksi menerima JSON datar dengan enam key persis (`area`, `item`, `year`, `average_rain_fall_mm_per_year`, `pesticides_tonnes`, `avg_temp`). Pydantic memvalidasi nilai, backend membuat DataFrame berurutan baku, menjalankan Pipeline sklearn dari `artifact["model"]` tepercaya, lalu mengembalikan `prediction_hg_ha`, `prediction_kg_ha`, `prediction_tonnes_ha`, dan disclaimer. Loading model di-cache dengan `lru_cache`. CORS dibatasi pada origin Vite lokal.


## Evidence / Bukti

- [Experiment notebook](../../notebooks/harvestforecast.ipynb)
- [Experiment metrics](../../reports/extracted/heldout_test_metrics.json)
- [Run configuration](../../reports/extracted/run_config.json)
- [Source inventory](../../reports/extracted/dataset_inventory.csv)
- [Limitations](limitations.md)
