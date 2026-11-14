# Dataset provenance and licensing

The training table is `df_yield_merged.csv` (1,290,988 bytes; SHA-256 `0a2b4e025610b5e9337dfdc49efd76472edba71d406954a63bdf091b58752e6e`). Four separately inventoried supporting files are `yield.csv`, `rainfall.csv`, `temp.csv` and `pesticides.csv`; they were audited, **not concatenated or rejoined** into the learning table. Kaggle mount: `/kaggle/input/datasets/wafabila/harvestforecast-dataset`, recorded access 2026-11-09 06:44 UTC.

The collection notes suggest `https://zenodo.org/records/18761663`, but exact file equivalence, original publication and license were **not independently verified** in the notebook. A Kaggle path is not an original license. Do not redistribute raw source data until permission, version, attribution and checksums are reconciled with the publisher.


## Evidence / Bukti

- [Experiment notebook](../../notebooks/harvestforecast.ipynb)
- [Experiment metrics](../../reports/extracted/heldout_test_metrics.json)
- [Run configuration](../../reports/extracted/run_config.json)
- [Source inventory](../../reports/extracted/dataset_inventory.csv)
- [Limitations](limitations.md)
