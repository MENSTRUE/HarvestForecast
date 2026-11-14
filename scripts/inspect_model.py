from pathlib import Path
import joblib
p=Path(__file__).resolve().parents[1]/'models'/'harvestforecast_champion.joblib'
print('Artifact:',p)
print('Exists:',p.exists())
if not p.exists(): raise SystemExit(1)
print('WARNING: Only load a trusted model artifact from your own training pipeline.')
m=joblib.load(p)
print('Type:',type(m).__name__)
print('Features:',list(getattr(m,'feature_names_in_',[])))
print('Pipeline steps:',list(getattr(m,'named_steps',{})))
