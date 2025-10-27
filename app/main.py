# app/main.py
# ----------------------------------------------
# FastAPI app - Heart Disease Prediction
# This file follows the instructor's style (lots of comments, multiple utility endpoints)
# ----------------------------------------------

from fastapi import FastAPI
import joblib
import os
import numpy as np
from .schemas import HeartInput, PredictionOutput

app = FastAPI(title="Heart Disease Prediction - FastAPI Masterclass")

# Model path (one level up from app/)
MODEL_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'model', 'heart_model.joblib')

# Global model variable
model = None

# Feature order - MUST match training features order used in model_run.py
FEATURE_ORDER = [
    "age","sex","cp","trestbps","chol","fbs","restecg",
    "thalach","exang","oldpeak","slope","ca","thal"
]

# -------------------------
# Startup - load model
# -------------------------
@app.on_event("startup")
def load_model():
    global model
    if not os.path.exists(MODEL_PATH):
        # If model missing, raise error - this makes debugging on deployment easier
        raise FileNotFoundError(f"Model file not found at {MODEL_PATH}. Please run training script to generate it.")
    model = joblib.load(MODEL_PATH)
    print("Model loaded from", MODEL_PATH)

# -------------------------
# Health check
# -------------------------
@app.get("/health")
def health_check():
    """
    Simple health endpoint
    """
    return {"status": "healthy"}

# -------------------------
# Info endpoint
# -------------------------
@app.get("/info")
def info():
    """
    Return basic info about model and features
    """
    model_type = type(model.named_steps['randomforestclassifier']).__name__ if hasattr(model, 'named_steps') and 'randomforestclassifier' in model.named_steps else str(type(model))
    return {
        "model": model_type,
        "features": FEATURE_ORDER
    }

# -------------------------
# Predict endpoint
# -------------------------
@app.post("/predict", response_model=PredictionOutput)
def predict(data: HeartInput):
    """
    Predict the presence of heart disease.
    Returns boolean 'heart_disease' and probability (if available).
    """
    # Convert incoming data to numpy array, respecting feature order
    arr = np.array([[
        data.age, data.sex, data.cp, data.trestbps, data.chol, data.fbs,
        data.restecg, data.thalach, data.exang, data.oldpeak, data.slope, data.ca, data.thal
    ]])

    # Predict
    prediction = model.predict(arr)
    prob = None
    if hasattr(model, "predict_proba"):
        prob = float(model.predict_proba(arr)[0, 1])

    # Convert to bool
    heart_disease = bool(int(prediction[0]))

    return {"heart_disease": heart_disease, "probability": prob}

# -------------------------
# Demo / Example (not required)
# -------------------------
@app.get("/")
def root():
    return {"message": "Heart Disease Prediction API. Use /docs for interactive swagger."}
