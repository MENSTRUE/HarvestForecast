# Asal data dan lisensi

Tabel training adalah `df_yield_merged.csv` (1.290.988 byte; SHA-256 `0a2b4e025610b5e9337dfdc49efd76472edba71d406954a63bdf091b58752e6e`). Empat sumber pendukung yang diinventarisasi terpisah adalah `yield.csv`, `rainfall.csv`, `temp.csv`, dan `pesticides.csv`; semuanya diaudit, **bukan digabung otomatis** ke tabel training. Mount Kaggle: `/kaggle/input/datasets/wafabila/harvestforecast-dataset`, akses tercatat 9 November 2026 pukul 06:44 UTC.

Catatan koleksi menunjuk `https://zenodo.org/records/18761663`, tetapi kesetaraan file, publikasi asli, dan lisensinya **belum diverifikasi independen** di notebook. Path Kaggle bukan bukti izin. Jangan distribusikan data mentah sebelum izin, versi, atribusi, dan checksum diverifikasi ke penerbit.


## Evidence / Bukti

- [Experiment notebook](../../notebooks/harvestforecast.ipynb)
- [Experiment metrics](../../reports/extracted/heldout_test_metrics.json)
- [Run configuration](../../reports/extracted/run_config.json)
- [Source inventory](../../reports/extracted/dataset_inventory.csv)
- [Limitations](limitations.md)
