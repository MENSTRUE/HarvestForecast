# Pemecahan masalah dan verifikasi

**Model unavailable:** pastikan `models/harvestforecast_champion.joblib` ada; file ini adalah **dictionary**, bukan estimator sklearn langsung. Periksa `artifact["kind"] == "sklearn_pipeline"`, `artifact["model"]`, `feature_names_in_`, target dan unit. Loader lama yang mengira artefak estimator langsung tidak cocok; `backend/app/main.py` yang diperiksa sekarang mengambil model dari dictionary.

**API tidak terhubung:** jalankan Uvicorn di port 8000; Vite mem-proxy `/api`. **HTTP 422:** cek JSON datar, rentang numerik, enam key tepat, dan ejaan kategori data latih. **Prediksi tidak finite/aneh:** bandingkan pembersihan data/preprocessing, unit, dan uji baris historis dengan input yang diketahui. **Build gagal:** `cd frontend; npm install; npm run build`. Jangan unpickle artefak dari sumber tidak tepercaya.


## Evidence / Bukti

- [Experiment notebook](../../notebooks/harvestforecast.ipynb)
- [Experiment metrics](../../reports/extracted/heldout_test_metrics.json)
- [Run configuration](../../reports/extracted/run_config.json)
- [Source inventory](../../reports/extracted/dataset_inventory.csv)
- [Limitations](limitations.md)
