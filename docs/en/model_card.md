# Model card — intended use, contract and safety

**Model:** validation-selected `random_forest_120`; regression, not classification. Saved bundle: `models/harvestforecast_champion.joblib` (dictionary with `kind="sklearn_pipeline"`, `model`, `features`, `target="value_hg_ha"`, `unit="hg/ha"`). The nested model is an sklearn Pipeline (`preprocess`, `regressor`).

**Intended use:** historic country/area × crop × year yield benchmarking where all six features are already observed. **Not intended:** prospective planting-time forecasts, farm-level guarantees, irrigation or pesticide recommendations, automated lending/insurance decisions. API predictions use original units, with exact conversions kg/ha = hg/ha ÷ 10 and tonnes/ha = hg/ha ÷ 10,000. This does not calculate total production without area in hectares. No field-level uncertainty intervals or calibration evidence are available.


## Evidence / Bukti

- [Experiment notebook](../../notebooks/harvestforecast.ipynb)
- [Experiment metrics](../../reports/extracted/heldout_test_metrics.json)
- [Run configuration](../../reports/extracted/run_config.json)
- [Source inventory](../../reports/extracted/dataset_inventory.csv)
- [Limitations](limitations.md)
