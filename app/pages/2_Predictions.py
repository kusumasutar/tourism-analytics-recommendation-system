# ============================================================
# Predictions Page
# ============================================================

import streamlit as st
import joblib

from pathlib import Path


# ------------------------------------------------------------
# Find project root
# ------------------------------------------------------------

BASE_DIR = (
    Path(__file__)
    .resolve()
    .parent
    .parent
    .parent
)

MODEL_DIR = (
    BASE_DIR / "models"
)


# ------------------------------------------------------------
# Page configuration
# ------------------------------------------------------------

st.set_page_config(
    page_title="Predictions",
    page_icon="🤖",
    layout="wide"
)


st.title("🤖 Tourism Prediction Models")

st.write(
    "This page loads the trained machine learning models "
    "created during the modeling stage."
)


# ------------------------------------------------------------
# Model paths
# ------------------------------------------------------------

classification_path = (
    MODEL_DIR /
    "classification_model.pkl"
)

regression_path = (
    MODEL_DIR /
    "regression_model.pkl"
)


# ------------------------------------------------------------
# Check files
# ------------------------------------------------------------

st.subheader(
    "Model Status"
)


col1, col2 = st.columns(2)


with col1:

    if classification_path.exists():

        st.success(
            "✅ Classification model found"
        )

    else:

        st.error(
            "❌ Classification model missing"
        )


with col2:

    if regression_path.exists():

        st.success(
            "✅ Regression model found"
        )

    else:

        st.error(
            "❌ Regression model missing"
        )


# ------------------------------------------------------------
# Load models
# ------------------------------------------------------------

if (
    classification_path.exists()
    and regression_path.exists()
):

    classification_model = joblib.load(
        classification_path
    )

    regression_model = joblib.load(
        regression_path
    )

    st.divider()

    st.subheader(
        "Classification Model"
    )

    st.write(
        "Predicts the expected visitor VisitMode."
    )

    st.info(
        "The trained classification model is loaded successfully."
    )

    st.subheader(
        "Regression Model"
    )

    st.write(
        "Predicts the expected attraction Rating."
    )

    st.info(
        "The trained regression model is loaded successfully."
    )

else:

    st.warning(
        "One or more trained models are missing. "
        "Please check the models folder."
    )