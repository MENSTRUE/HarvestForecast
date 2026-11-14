# Deployment dan kesiapan operasional

**Status saat ini:** prototipe riset yang didemonstrasikan secara lokal. Pengguna menunjukkan screenshot status model online, tetapi belum ada hasil prediksi yang dikirim, tes integrasi otomatis, atau URL deployment publik yang terverifikasi independen. Source GitHub belum memuat infrastructure-as-code, CI deployment, atau autentikasi.

Dari root repo di PowerShell: `& "C:\DevEnvs\ai-general\Scripts\python.exe" -m pip install -r backend\requirements.txt` lalu `& "C:\DevEnvs\ai-general\Scripts\python.exe" -m uvicorn backend.app.main:app --reload --port 8000`; terminal lain: `cd frontend; npm install; npm run dev`. Cek `http://127.0.0.1:8000/docs` dan `http://127.0.0.1:5173`. Sebelum deploy publik: kunci/audit dependency, matikan reload debug, tambah autentikasi/rate limit/log/monitoring, pastikan kategori input, validasi eksternal, ketersediaan fitur dan lisensi.


## Evidence / Bukti

- [Experiment notebook](../../notebooks/harvestforecast.ipynb)
- [Experiment metrics](../../reports/extracted/heldout_test_metrics.json)
- [Run configuration](../../reports/extracted/run_config.json)
- [Source inventory](../../reports/extracted/dataset_inventory.csv)
- [Limitations](limitations.md)
