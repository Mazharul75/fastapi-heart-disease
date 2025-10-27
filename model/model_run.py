# model/model_run.py
# ----------------------------------------------
# Train & save a model for Heart Disease
# This file follows the same style & structure as the instructor's iris example
# ----------------------------------------------

import os
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

# Paths
DATA_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'heart.csv')  # project_root/heart.csv
MODEL_DIR = os.path.join(os.path.dirname(__file__))
MODEL_PATH = os.path.join(MODEL_DIR, 'heart_model.joblib')

def run_training():
    """
    Train a RandomForest classifier on the Heart Disease dataset and save model.
    Expects a CSV file at project_root/heart.csv
    """
    if not os.path.exists(DATA_PATH):
        raise FileNotFoundError(f"Dataset not found at {DATA_PATH}. Download the Kaggle heart CSV and place it there.")

    print("Loading dataset:", DATA_PATH)
    df = pd.read_csv(DATA_PATH)
    print("Initial dataframe shape:", df.shape)

    # Identify target column - common names: 'target' or 'HeartDisease' or 'heart_disease'
    if 'target' in df.columns:
        y = df['target']
        X = df.drop(columns=['target'])
    elif 'HeartDisease' in df.columns:
        y = df['HeartDisease']
        X = df.drop(columns=['HeartDisease'])
    elif 'heart_disease' in df.columns:
        y = df['heart_disease']
        X = df.drop(columns=['heart_disease'])
    else:
        raise KeyError("Cannot find target column. Expected 'target' or 'HeartDisease' or 'heart_disease'.")

    # Basic cleaning: drop rows with NA
    df = df.dropna()
    print("After dropna shape:", df.shape)

    # Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)
    print("Train shape:", X_train.shape, "Test shape:", X_test.shape)

    # Pipeline (scaler + RandomForest)
    pipeline = make_pipeline(StandardScaler(), RandomForestClassifier(n_estimators=100, random_state=42))
    print("Training model...")
    pipeline.fit(X_train, y_train)

    # Print accuracy
    acc = pipeline.score(X_test, y_test)
    print(f"Test accuracy: {acc:.4f}")

    # Save model
    os.makedirs(MODEL_DIR, exist_ok=True)
    joblib.dump(pipeline, MODEL_PATH)
    print(f"Model saved to {MODEL_PATH}")

if __name__ == '__main__':
    run_training()
