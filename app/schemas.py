# app/schemas.py
# ----------------------------------------------
# Pydantic schemas for Heart Disease API
# Mirrors the instructor's simple schema style
# ----------------------------------------------

from pydantic import BaseModel

# Input schema for /predict
class HeartInput(BaseModel):
    age: float
    sex: int
    cp: int
    trestbps: float
    chol: float
    fbs: int
    restecg: int
    thalach: float
    exang: int
    oldpeak: float
    slope: int
    ca: float
    thal: float

# Output schema for /predict
class PredictionOutput(BaseModel):
    heart_disease: bool
    probability: float | None = None
