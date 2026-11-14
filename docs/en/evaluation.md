# Temporal evaluation and error analysis

Train **1990–2005, 8,444 rows**; validation **2006–2009, 2,331**; held-out test **2010–2013, 2,355**. Year sets do not overlap, but 581 area/crop pairs recur from train into validation and 580 into test. This assesses later historical years, not geographical out-of-distribution performance.

The held-out file records MAE **16,393.5078 hg/ha**, RMSE **30,993.0784 hg/ha**, R² **0.874259**, WAPE **20.1561%**. Error varies: test MAE Sweet potatoes 33,793.67 (n=206), Cassava 32,048.09 (n=164), Soybeans 3,353.48 (n=227); by year it increases from 13,991.07 (2010) to 18,455.28 (2013). These are descriptive findings, not license to tune on the held-out test. Regression has no confusion matrix or per-class recall; use residual plots and group-wise MAE.


## Evidence / Bukti

- [Experiment notebook](../../notebooks/harvestforecast.ipynb)
- [Experiment metrics](../../reports/extracted/heldout_test_metrics.json)
- [Run configuration](../../reports/extracted/run_config.json)
- [Source inventory](../../reports/extracted/dataset_inventory.csv)
- [Limitations](limitations.md)
