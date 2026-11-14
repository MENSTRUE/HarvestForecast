# Evaluasi temporal dan analisis kesalahan

Train **1990–2005, 8.444 baris**; validation **2006–2009, 2.331**; held-out test **2010–2013, 2.355**. Tahun tidak tumpang tindih, tetapi 581 pasangan area/tanaman berulang dari train ke validation dan 580 ke test. Ini menilai tahun historis lebih baru, bukan generalisasi ke wilayah baru.

File held-out mencatat MAE **16.393,5078 hg/ha**, RMSE **30.993,0784 hg/ha**, R² **0,874259**, WAPE **20,1561%**. Error berbeda: MAE test Sweet potatoes 33.793,67 (n=206), Cassava 32.048,09 (n=164), Soybeans 3.353,48 (n=227); per tahun naik dari 13.991,07 (2010) menjadi 18.455,28 (2013). Ini deskripsi, bukan alasan tuning memakai test. Regresi tidak memakai confusion matrix atau recall per kelas; gunakan plot residual dan MAE per grup.


## Evidence / Bukti

- [Experiment notebook](../../notebooks/harvestforecast.ipynb)
- [Experiment metrics](../../reports/extracted/heldout_test_metrics.json)
- [Run configuration](../../reports/extracted/run_config.json)
- [Source inventory](../../reports/extracted/dataset_inventory.csv)
- [Limitations](limitations.md)
