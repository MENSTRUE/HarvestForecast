# Utility scripts

[`inspect_model.py`](inspect_model.py) is the currently tracked inspection helper. **Caveat:** at the checked GitHub revision, it prints model metadata on the outer joblib dictionary, which has no direct `feature_names_in_`. It may therefore print empty `Features` although the nested pipeline is valid. This script has not been silently modified by documentation changes.

A trustworthy inspection must first check `bundle['kind'] == 'sklearn_pipeline'`, then inspect `bundle['model'].feature_names_in_`, `bundle['features']`, `bundle['target']` and `bundle['unit']`. Use the fixed backend loader in `backend/app/main.py` as reference. Run only against trusted locally trained joblib artifacts. See [troubleshooting](../docs/en/troubleshooting.md).
