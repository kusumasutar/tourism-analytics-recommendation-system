# ============================================================
# Recommendations Page
# ============================================================

import streamlit as st
import pandas as pd

from pathlib import Path
import sys


# ------------------------------------------------------------
# Allow Python to find our utility files
# ------------------------------------------------------------

APP_DIR = Path(__file__).resolve().parent.parent

sys.path.append(
    str(APP_DIR)
)


from utils.data_loader import (
    load_cleaned_data,
    load_recommendation_system
)

from utils.recommendation import recommend


# ------------------------------------------------------------
# Page configuration
# ------------------------------------------------------------

st.set_page_config(
    page_title="Recommendations",
    page_icon="🎯",
    layout="wide"
)


st.title("🎯 Attraction Recommendation System")

st.write(
    "Get personalized tourism attraction recommendations."
)


# ------------------------------------------------------------
# Load data
# ------------------------------------------------------------

@st.cache_data
def get_data():

    return load_cleaned_data()


@st.cache_resource
def get_recommendation_system():

    return load_recommendation_system()


try:

    df = get_data()

    recommendation_objects = (
        get_recommendation_system()
    )

except Exception as e:

    st.error(
        "Unable to load recommendation files."
    )

    st.exception(e)

    st.stop()


# ------------------------------------------------------------
# Retrieve recommendation objects
# ------------------------------------------------------------

user_item_matrix = (
    recommendation_objects[
        "user_item_matrix"
    ]
)

item_similarity_df = (
    recommendation_objects[
        "item_similarity_df"
    ]
)

attraction_info = (
    recommendation_objects[
        "attraction_info"
    ]
)


# ------------------------------------------------------------
# User input
# ------------------------------------------------------------

st.subheader("Enter User Details")

user_id = st.number_input(
    "User ID",
    min_value=1,
    step=1,
    value=int(
        user_item_matrix.index[0]
    )
)

number_of_recommendations = st.slider(
    "Number of recommendations",
    min_value=1,
    max_value=10,
    value=5
)


# ------------------------------------------------------------
# Generate recommendations
# ------------------------------------------------------------

if st.button(
    "🎯 Get Recommendations",
    type="primary"
):

    results = recommend(
        user_id=int(user_id),
        n=number_of_recommendations,
        user_item_matrix=user_item_matrix,
        item_similarity_df=item_similarity_df,
        attraction_info=attraction_info
    )

    if results.empty:

        st.warning(
            "This user does not have enough "
            "rating history for collaborative filtering."
        )

        st.info(
            "Try another User ID."
        )

    else:

        st.subheader(
            "Recommended Attractions"
        )

        # Display each recommendation as a card
        for index, row in results.iterrows():

            st.markdown(
                f"### {index + 1}. {row['Attraction']}"
            )

            col1, col2, col3 = st.columns(3)

            with col1:

                st.write(
                    f"**Type:** "
                    f"{row['AttractionType']}"
                )

            with col2:

                st.write(
                    f"**Location:** "
                    f"{row['CityName']}"
                )

            with col3:

                st.write(
                    f"**Country:** "
                    f"{row['Country']}"
                )

            st.write(
                f"Recommendation Score: "
                f"{row['RecommendationScore']:.3f}"
            )

            st.divider()