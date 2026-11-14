# Research reports and evidence inventory

`extracted/` contains experiment outputs from the Day 37 Kaggle results archive. Treat reports as recorded experimental evidence, not a guarantee of field generalization.

| Artifact | What it supports |
|---|---|
| [`dataset_audit.json`](extracted/dataset_audit.json) | 25,932 source rows; 13,130 retained; key de-duplication |
| [`dataset_provenance.json`](extracted/dataset_provenance.json) | Source names, checksums, unresolved licensing |
| [`schema_audit.csv`](extracted/schema_audit.csv) | Source columns, types, missing values |
| [`split_audit.json`](extracted/split_audit.json) | Chronological year boundaries and recurring area/crop pairs |
| [`validation_leaderboard.csv`](extracted/validation_leaderboard.csv) | Seven candidate comparisons; MAE-based champion |
| [`model_selection.json`](extracted/model_selection.json) | Frozen winner before test |
| [`heldout_test_metrics.json`](extracted/heldout_test_metrics.json) | Final MAE, RMSE, R² and WAPE |
| [`heldout_test_mae_by_crop.csv`](extracted/heldout_test_mae_by_crop.csv) | Crop-specific errors |
| [`heldout_test_mae_by_year.csv`](extracted/heldout_test_mae_by_year.csv) | Later-year drift diagnostics |
| [`run_config.json`](extracted/run_config.json) | Exact feature list, target and seed |
| [`artifact_manifest.json`](extracted/artifact_manifest.json) | Exported files and hashes |
| [`MODEL_CARD.md`](extracted/MODEL_CARD.md) | Original experiment model card; preserved |

The three split manifests contain hashed observation keys, not raw feature columns; the archive's original sample-error CSVs are part of extracted results, not evidence of deployment. `extraction_manifest.json` documents local extraction. See [evaluation](../docs/en/evaluation.md).
