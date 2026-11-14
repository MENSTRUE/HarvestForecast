# Reproduksibilitas dan asal eksperimen

Sumber acuan: `notebooks/harvestforecast.ipynb` untuk transformasi; `reports/extracted/run_config.json` untuk seed `42` dan daftar fitur; `dataset_inventory.csv` serta `dataset_provenance.json` untuk hash; `split_audit.json` untuk batas tahun; `validation_leaderboard.csv` untuk seleksi; `heldout_test_metrics.json` untuk skor akhir.

Untuk reproduksi, mount lima CSV bernama sama di Kaggle pada `/kaggle/input/datasets/wafabila/harvestforecast-dataset`, jalankan notebook dari kernel bersih dan bandingkan hash/split dengan laporan. SHA-256 artefak pada `artifact_manifest.json` adalah `2ac6e5aca35241065cfb93f78f70181fad740aa8dfc6e7c1f237233b528611f0`; perbedaan berarti binary berbeda. Reproduksi tetap bergantung pada verifikasi versi data, versi package dan lisensi; hasil rerun identik belum diverifikasi independen.


## Evidence / Bukti

- [Experiment notebook](../../notebooks/harvestforecast.ipynb)
- [Experiment metrics](../../reports/extracted/heldout_test_metrics.json)
- [Run configuration](../../reports/extracted/run_config.json)
- [Source inventory](../../reports/extracted/dataset_inventory.csv)
- [Limitations](limitations.md)
