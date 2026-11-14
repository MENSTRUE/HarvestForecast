from __future__ import annotations
import json
import os
from functools import lru_cache
from pathlib import Path
from typing import Any
import joblib
import numpy as np
import pandas as pd
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field, ConfigDict

ROOT = Path(__file__).resolve().parents[2]
MODEL_PATH = ROOT / 'models' / 'harvestforecast_champion.joblib'
CONFIG_PATH = ROOT / 'reports' / 'extracted' / 'run_config.json'
METRICS_PATH = ROOT / 'reports' / 'extracted' / 'heldout_test_metrics.json'
EXPECTED = ['area','item','year','average_rain_fall_mm_per_year','pesticides_tonnes','avg_temp']
app = FastAPI(title='HarvestForecast API', version='1.0.0', description='Retrospective agricultural yield estimation')
app.add_middleware(CORSMiddleware,allow_origins=['http://localhost:5173','http://127.0.0.1:5173'],allow_credentials=False,allow_methods=['GET','POST'],allow_headers=['Content-Type'])

class PredictionRequest(BaseModel):
    model_config = ConfigDict(extra='forbid', str_strip_whitespace=True)
    area: str = Field(min_length=1,max_length=120)
    item: str = Field(min_length=1,max_length=120)
    year: int = Field(ge=1900,le=2100)
    average_rain_fall_mm_per_year: float = Field(ge=0,le=30000,allow_inf_nan=False)
    pesticides_tonnes: float = Field(ge=0,le=100000000,allow_inf_nan=False)
    avg_temp: float = Field(ge=-80,le=70,allow_inf_nan=False)

@lru_cache(maxsize=1)
def get_model():
    # Load only the trusted local training artifact.
    if not MODEL_PATH.is_file():
        raise FileNotFoundError(
            f"Model missing: {MODEL_PATH}"
        )

    artifact = joblib.load(MODEL_PATH)

    if not isinstance(artifact, dict):
        raise TypeError(
            "Expected a training artifact dictionary"
        )

    if artifact.get("kind") != "sklearn_pipeline":
        raise ValueError(
            f"Unsupported artifact kind: {artifact.get('kind')}"
        )

    model = artifact.get("model")
    features = artifact.get("features")
    target = artifact.get("target")
    unit = artifact.get("unit")

    if model is None or not hasattr(model, "predict"):
        raise TypeError(
            "Artifact does not contain a valid predictive model"
        )

    if list(features or []) != EXPECTED:
        raise ValueError(
            f"Artifact features differ from API: {features}"
        )

    if target != "value_hg_ha":
        raise ValueError(
            f"Unexpected target: {target}"
        )

    if unit != "hg/ha":
        raise ValueError(
            f"Unexpected target unit: {unit}"
        )

    actual = getattr(model, "feature_names_in_", None)

    if actual is None:
        raise ValueError(
            "Cannot verify pipeline feature names"
        )

    if list(actual) != EXPECTED:
        raise ValueError(
            f"Pipeline feature order differs: {list(actual)}"
        )

    return model


def read_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding='utf-8'))
    except (OSError,ValueError):
        return {}

@app.get('/api/v1/health')
def health():
    try:
        get_model()
        return {'status':'ok','model_ready':True,'model':'harvestforecast_champion.joblib'}
    except Exception as exc:
        return {'status':'degraded','model_ready':False,'reason':str(exc)}

@app.get('/api/v1/model')
def metadata():
    status=health()
    config=read_json(CONFIG_PATH)
    metrics=read_json(METRICS_PATH)
    return {'health':status,'features':EXPECTED,'target':'value_hg_ha','target_unit':'hg/ha',
      'champion':config.get('champion'),'metrics':metrics,
      'limitations':['Retrospective benchmark, not a validated pre-season forecast','Annual weather/pesticide inputs may be unavailable before harvest','Area-level aggregate estimates do not predict individual field yield'],
      'category_note':'Area and item must match categories learned by the model; unknown values may cause an error or unreliable output.'}

@app.post('/api/v1/predict')
def predict(payload: PredictionRequest):
    try:
        model=get_model()
    except Exception as exc:
        raise HTTPException(status_code=503,detail=f'Model unavailable: {exc}')
    frame=pd.DataFrame([payload.model_dump()],columns=EXPECTED)
    try:
        raw=model.predict(frame)
        value=float(np.asarray(raw).reshape(-1)[0])
        if not np.isfinite(value):
            raise ValueError('Non-finite prediction')
    except (ValueError,TypeError,KeyError) as exc:
        raise HTTPException(status_code=422,detail=f'Inference rejected: {exc}')
    except Exception:
        raise HTTPException(status_code=500,detail='Model inference failed. Inspect backend logs.')
    return {'prediction_hg_ha':value,'prediction_kg_ha':value/10,'prediction_tonnes_ha':value/10000,
            'unit':'hg/ha','model':'harvestforecast_champion.joblib',
            'disclaimer':'Retrospective country/crop/year yield estimate, not an operational pre-season forecast.'}
