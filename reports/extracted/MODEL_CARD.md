# HarvestForecast — Day 37 Model Card

## Task
Retrospective country/area × crop × year agricultural yield regression.

## Dataset
`df_yield_merged.csv` inside HarvestForecast Kaggle input; other four CSVs audited only and not automatically rejoined.

## Outcome
`value_hg_ha` in **hg/ha**. Champion `random_forest_120` selected exclusively using validation **MAE**.

## Split
Train 1990–2005 (8,444 records); validation 2006–2009 (2,331); held-out test 2010–2013 (2,355).

## Held-out metrics (not used for tuning)
MAE **16,393.508 hg/ha**; RMSE **30,993.078 hg/ha**; R² **0.8743**.

## Limitations
- Weather and pesticide variables for a target year may be **post-hoc**, not available at planting time.
- Country-level/area-level aggregates cannot be assumed valid for individual fields.
- Area/crop identities may overlap across years; generalization to unseen locations is not measured.
- Records may inherit unverified original collection methods, licenses and measurement noise.
- Climate shifts, nonstationarity and data availability can degrade future-year performance.
- Do not treat yield predictions as guarantees or automatically recommend resource input levels.
- Historical median baseline is not a trained neural network and has a different inference implementation.

## Reproduction
Seed `42`. `run_config.json`, `dataset_inventory.csv`, `dataset_audit.json`, `split_audit.json`, leaderboard, per-crop and per-year evaluation and plot artifacts are emitted next to this card.
