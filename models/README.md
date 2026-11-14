# Saved model — trusted local artifact

`harvestforecast_champion.joblib` is a **7,532,170-byte** joblib dictionary, SHA-256 `2ac6e5aca35241065cfb93f78f70181fad740aa8dfc6e7c1f237233b528611f0` in the recorded manifest. Its fields are `kind`, `model`, `features`, `target`, `unit`. `kind=sklearn_pipeline`, `target=value_hg_ha`, `unit=hg/ha`. The nested `model` is a fitted sklearn Pipeline with `preprocess` and `regressor` steps; **do not** call `.predict()` on the surrounding dictionary.

Ordered features: `area`, `item`, `year`, `average_rain_fall_mm_per_year`, `pesticides_tonnes`, `avg_temp`. The trained regression model is `random_forest_120`, validation-selected with MAE 11,232.15 hg/ha; held-out MAE 16,393.51 hg/ha over 2,355 later-year records. No confidence intervals or future-year external validation are provided.

Load only a trusted model file: pickle deserialization can execute code. Inspect schema and hashes against [experiment config](../reports/extracted/run_config.json), [manifest](../reports/extracted/artifact_manifest.json) and [model card](../docs/en/model_card.md). Do not replace the artifact to change behavior without rerunning evaluation and updating the full lineage.
