# Reproducibility and lineage

Source of truth: `notebooks/harvestforecast.ipynb` for transformations; `reports/extracted/run_config.json` for seed `42` and feature list; `dataset_inventory.csv` and `dataset_provenance.json` for file hashes; `split_audit.json` for year boundaries; `validation_leaderboard.csv` for selection; `heldout_test_metrics.json` for final scores.

To reproduce, mount the five named source CSVs in Kaggle at `/kaggle/input/datasets/wafabila/harvestforecast-dataset`, run the notebook from a clean kernel and compare generated hashes/splits against committed reports. The artifact SHA-256 listed in `artifact_manifest.json` is `2ac6e5aca35241065cfb93f78f70181fad740aa8dfc6e7c1f237233b528611f0`; a mismatch indicates a different binary. Reproduction still depends on verifying source version, package versions and origin licensing; rerun equivalence has not been independently established.


## Evidence / Bukti

- [Experiment notebook](../../notebooks/harvestforecast.ipynb)
- [Experiment metrics](../../reports/extracted/heldout_test_metrics.json)
- [Run configuration](../../reports/extracted/run_config.json)
- [Source inventory](../../reports/extracted/dataset_inventory.csv)
- [Limitations](limitations.md)
