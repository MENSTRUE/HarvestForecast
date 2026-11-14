# Limitations, interpretation boundaries and threats to validity

The strongest limitation is **feature availability**: annual rain, temperature and pesticide usage can be finalized only after the year/harvest. Calling this pre-season forecast would leak future information at decision time, even though the chronological evaluation does not mix years.

Area-level statistics cannot be applied directly to specific fields. Area/crop pairs overlap across periods; zero geographic OOD evidence. Unknown categories are ignored by the model encoder and may give plausible but unreliable predictions. Climate shift, missing data in future periods, measurement procedures and crop-specific error differences require separate prospective validation. Upstream dataset license and equivalence are unverified; no public production deployment, farm pilot, interval coverage or automated decision safety review has been demonstrated.


## Evidence / Bukti

- [Experiment notebook](../../notebooks/harvestforecast.ipynb)
- [Experiment metrics](../../reports/extracted/heldout_test_metrics.json)
- [Run configuration](../../reports/extracted/run_config.json)
- [Source inventory](../../reports/extracted/dataset_inventory.csv)
- [Limitations](limitations.md)
