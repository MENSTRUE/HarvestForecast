# Metodologi dan pencegahan leakage

Masalah penelitian adalah **regresi retrospektif** untuk `value_hg_ha` (hektogram per hektare). Tepat enam prediktor dipakai: `area`, `item`, `year`, `average_rain_fall_mm_per_year`, `pesticides_tonnes`, dan `avg_temp`. Kolom turunan target dikecualikan. Hanya CSV utama yang sudah digabung sebelumnya dipakai untuk supervised learning.

Notebook menolak yield tidak valid/nol, area/tanaman kosong, dan tahun salah; memeriksa duplikat serta pengulangan key (`area`,`item`,`year`); mengarantina target yang konflik; menyimpan satu observasi per key. Dari 25.932 baris sumber, tersisa 13.130 setelah membuang 12.802 baris key berulang. `Pipeline` sklearn melakukan imputasi kategorikal, one-hot encoding, imputasi median numerik dan scaling yang dipelajari dari train saja; kemudian regressor dilatih. One-hot memakai `handle_unknown="ignore"`, sehingga kategori area/tanaman baru dapat menghasilkan angka tanpa jaminan keandalannya.


## Evidence / Bukti

- [Experiment notebook](../../notebooks/harvestforecast.ipynb)
- [Experiment metrics](../../reports/extracted/heldout_test_metrics.json)
- [Run configuration](../../reports/extracted/run_config.json)
- [Source inventory](../../reports/extracted/dataset_inventory.csv)
- [Limitations](limitations.md)
