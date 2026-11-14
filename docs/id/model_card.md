# Kartu model — tujuan, kontrak, keselamatan

**Model:** `random_forest_120` hasil seleksi validation; regresi, bukan klasifikasi. Bundel: `models/harvestforecast_champion.joblib` (dictionary dengan `kind="sklearn_pipeline"`, `model`, `features`, `target="value_hg_ha"`, `unit="hg/ha"`). Model dalam bundel adalah Pipeline sklearn (`preprocess`, `regressor`).

**Penggunaan yang sesuai:** pembandingan hasil panen historis tingkat wilayah × tanaman × tahun saat keenam fitur sudah diketahui. **Bukan untuk:** prediksi sebelum tanam, jaminan yield per lahan, rekomendasi irigasi/pestisida, keputusan otomatis pinjaman/asuransi. API mengembalikan unit asli, dengan konversi kg/ha = hg/ha ÷ 10 dan ton/ha = hg/ha ÷ 10.000. Ini tidak menghitung total produksi tanpa luas hektare. Belum ada interval ketidakpastian atau kalibrasi lapangan.


## Evidence / Bukti

- [Experiment notebook](../../notebooks/harvestforecast.ipynb)
- [Experiment metrics](../../reports/extracted/heldout_test_metrics.json)
- [Run configuration](../../reports/extracted/run_config.json)
- [Source inventory](../../reports/extracted/dataset_inventory.csv)
- [Limitations](limitations.md)
