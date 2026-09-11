# ============================================================
# Tourism Analytics
# Main Streamlit Application
# ============================================================

import streamlit as st


# ------------------------------------------------------------
# Page configuration
# ------------------------------------------------------------

st.set_page_config(
    page_title="Tourism Analytics",
    page_icon="🌍",
    layout="wide"
)


# ------------------------------------------------------------
# Home page
# ------------------------------------------------------------

st.title("🌍 Tourism Analytics & Recommendation System")

st.write(
    "Welcome to the Tourism Analytics application."
)

st.markdown(
    """
    ### What can you do?

    **🎯 Recommendations**
    
    Get personalized attraction recommendations
    based on user history.

    **🤖 Predictions**
    
    Predict the visitor's expected visit mode
    and attraction rating.

    **📊 Analytics**
    
    Explore tourism trends, popular attractions,
    regions and visitor behavior.
    """
)

st.divider()

st.subheader("Project Overview")

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        "Tourism Transactions",
        "52,930"
    )

with col2:

    st.metric(
        "Users",
        "33,530"
    )

with col3:

    st.metric(
        "Attractions",
        "30"
    )

st.info(
    "Use the pages in the sidebar to explore "
    "recommendations, predictions and analytics."
)