# Eksperimen kandidat dan pemilihan model

Training memakai seed `42`. Kandidat: median historis area–tanaman, dummy median, Ridge alpha 1 dan 100, Random Forest 120 atau 200 pohon, serta HistGradientBoosting. Champion dipilih **hanya dari MAE validation** (lebih kecil lebih baik); pada nilai sama kode mengurutkan RMSE lalu nama model.

MAE validasi (hg/ha): `random_forest_120` **11.232,15**; `random_forest_200` 12.967,59; median historis 15.518,21; HistGB 16.282,15; Ridge alpha 1 29.866,23; Ridge alpha 100 31.028,57; dummy median 56.412,69. Pemenang memakai `RandomForestRegressor(n_estimators=120, min_samples_leaf=3, max_features=0.8, n_jobs=-1, random_state=42)`. Setelah pemilihan, training tidak diulang pada validation atau held-out test.


## Evidence / Bukti

- [Experiment notebook](../../notebooks/harvestforecast.ipynb)
- [Experiment metrics](../../reports/extracted/heldout_test_metrics.json)
- [Run configuration](../../reports/extracted/run_config.json)
- [Source inventory](../../reports/extracted/dataset_inventory.csv)
- [Limitations](limitations.md)
