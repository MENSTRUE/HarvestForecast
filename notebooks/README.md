# Notebook — reproducible Kaggle experiment

[`harvestforecast.ipynb`](harvestforecast.ipynb) covers: data inventory and hash/provenance audit, target identification, de-duplication of area/crop/year keys, feature/missingness checks, EDA, strict year-based train/validation/test partitioning, sklearn preprocessing, seven candidate/baseline comparisons, validation-only champion selection, final held-out evaluation and joblib export. The notebook is the source of truth for precise data treatment and hyperparameters.

Run on Kaggle CPU with input mounted at `/kaggle/input/datasets/wafabila/harvestforecast-dataset`; source files: `df_yield_merged.csv`, `yield.csv`, `rainfall.csv`, `temp.csv`, `pesticides.csv`. Output is written under `/kaggle/working/HarvestForecast_Day37`. The supplied results do **not** redistribute raw input CSVs.

Inspect [source hashes](../reports/extracted/dataset_provenance.json), [split audit](../reports/extracted/split_audit.json), [validation ranking](../reports/extracted/validation_leaderboard.csv), and [held-out scores](../reports/extracted/heldout_test_metrics.json). Do not choose the champion using held-out results. Consult [reproducibility guide](../docs/en/reproducibility.md) for limitations.
