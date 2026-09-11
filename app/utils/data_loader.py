# ============================================================
# data_loader.py
#
# This file contains functions used to load project data
# and trained models.
# ============================================================

from pathlib import Path
import pandas as pd
import joblib


# ------------------------------------------------------------
# Find the project root
# ------------------------------------------------------------

# data_loader.py is located inside:
#
# tourism-analytics/
#     app/
#         utils/
#             data_loader.py
#
# Therefore:
# parent      -> utils
# parent.parent -> app
# parent.parent.parent -> project root

BASE_DIR = Path(__file__).resolve().parent.parent.parent

DATA_DIR = BASE_DIR / "data/processed"
MODEL_DIR = BASE_DIR / "models"


# ------------------------------------------------------------
# Load cleaned tourism data
# ------------------------------------------------------------

def load_cleaned_data():

    # Expected location of the cleaned dataset
    file_path = DATA_DIR / "cleaned_data.csv"

    # Give a clear error if the file is missing
    if not file_path.exists():

        raise FileNotFoundError(
            f"Cleaned dataset was not found.\n"
            f"Expected location:\n{file_path}\n\n"
            f"Please make sure cleaned_data.csv exists "
            f"inside the data folder."
        )

    return pd.read_csv(file_path)


# ------------------------------------------------------------
# Load recommendation system
# ------------------------------------------------------------

def load_recommendation_system():

    file_path = MODEL_DIR / "recommendation_system.pkl"

    if not file_path.exists():

        raise FileNotFoundError(
            f"Recommendation model was not found:\n"
            f"{file_path}"
        )

    return joblib.load(file_path)


# ------------------------------------------------------------
# Load classification model
# ------------------------------------------------------------

def load_classification_model():

    file_path = MODEL_DIR / "classification_model.pkl"

    if not file_path.exists():

        raise FileNotFoundError(
            f"Classification model was not found:\n"
            f"{file_path}"
        )

    return joblib.load(file_path)


# ------------------------------------------------------------
# Load regression model
# ------------------------------------------------------------

def load_regression_model():

    file_path = MODEL_DIR / "regression_model.pkl"

    if not file_path.exists():

        raise FileNotFoundError(
            f"Regression model was not found:\n"
            f"{file_path}"
        )

    return joblib.load(file_path)