# Candidate experiments and model selection

Training uses seed `42`. Candidate set: historical area–crop median, dummy median, Ridge alpha 1 and 100, Random Forest with 120 or 200 trees, and HistGradientBoosting. The champion is selected **only on validation MAE** (smaller is better); tie-breaking in the code sorts RMSE then model name.

Validation MAE (hg/ha): `random_forest_120` **11,232.15**; `random_forest_200` 12,967.59; historical median 15,518.21; HistGB 16,282.15; Ridge alpha 1 29,866.23; Ridge alpha 100 31,028.57; dummy median 56,412.69. The winner uses `RandomForestRegressor(n_estimators=120, min_samples_leaf=3, max_features=0.8, n_jobs=-1, random_state=42)`. Training rows are not refit with validation or held-out test after selection.


## Evidence / Bukti

- [Experiment notebook](../../notebooks/harvestforecast.ipynb)
- [Experiment metrics](../../reports/extracted/heldout_test_metrics.json)
- [Run configuration](../../reports/extracted/run_config.json)
- [Source inventory](../../reports/extracted/dataset_inventory.csv)
- [Limitations](limitations.md)
