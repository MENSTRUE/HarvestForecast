# Methodology and leakage controls

The research problem is **retrospective regression** of `value_hg_ha` (hectograms per hectare). Exactly six predictors are used: `area`, `item`, `year`, `average_rain_fall_mm_per_year`, `pesticides_tonnes`, and `avg_temp`. Target-derived columns are excluded. Only the already-merged primary CSV is used for supervised learning.

The notebook rejects invalid/zero yield, empty area/crop and malformed year; checks exact duplicates and repeated (`area`,`item`,`year`) keys; quarantines conflicting targets; and retains one observation per key. From 25,932 source rows, 13,130 remain after removing 12,802 repeated-key rows. The full sklearn `Pipeline` fits category imputation and one-hot encoding, numerical median imputation and scaling on training data only; the regressor is fitted after preprocessing. One-hot encoding uses `handle_unknown="ignore"`, so unknown area/crop may produce a number without proof of reliability.


## Evidence / Bukti

- [Experiment notebook](../../notebooks/harvestforecast.ipynb)
- [Experiment metrics](../../reports/extracted/heldout_test_metrics.json)
- [Run configuration](../../reports/extracted/run_config.json)
- [Source inventory](../../reports/extracted/dataset_inventory.csv)
- [Limitations](limitations.md)
