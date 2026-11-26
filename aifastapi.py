# app/main.py

from pathlib import Path

from typing import Literal

 

import joblib

import pandas as pd

from fastapi import FastAPI, HTTPException

from pydantic import BaseModel, Field

 

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "model_artifacts" / "model.joblib"

MODEL_VERSION = "1.0.0"

THRESHOLD = 0.5  # use the threshold you chose in Module 5

 

app = FastAPI(title="Project Prediction API", version=MODEL_VERSION)

MODEL = joblib.load(MODEL_PATH)  # loaded once, at startup

 

 

class PredictionInput(BaseModel):

    loan_amount: float = Field(..., gt=0, description="Requested amount (ETB)")

    monthly_income: float = Field(..., ge=0, description="Monthly income (ETB)")

    credit_score: int = Field(..., ge=300, le=850, description="Credit bureau score")

    loan_type: Literal["agricultural", "business", "personal"]

 

 

class PredictionOutput(BaseModel):

    probability: float

    risk_label: Literal["high_risk", "low_risk"]

    model_version: str

 

 

@app.get("/health")

def health():

    return {"status": "healthy", "model_version": MODEL_VERSION}

 

 

@app.post("/predict", response_model=PredictionOutput)

def predict(item: PredictionInput):

    try:

        df = pd.DataFrame([item.model_dump()])

        prob = float(MODEL.predict_proba(df)[0][1])

    except Exception as exc:

        raise HTTPException(status_code=500, detail="Prediction failed") from exc

 

    return PredictionOutput(

        probability=round(prob, 4),

        risk_label="high_risk" if prob >= THRESHOLD else "low_risk",

        model_version=MODEL_VERSION,

    )