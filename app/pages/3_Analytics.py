# ============================================================
# Analytics Page
# ============================================================

import streamlit as st
import pandas as pd


# ------------------------------------------------------------
# Page configuration
# ------------------------------------------------------------

st.set_page_config(
    page_title="Tourism Analytics",
    page_icon="📊",
    layout="wide"
)


st.title("📊 Tourism Analytics Dashboard")


# ------------------------------------------------------------
# Load data
# ------------------------------------------------------------

@st.cache_data
def load_data():

    return pd.read_csv(
        "data/processed/cleaned_data.csv"
    )


try:

    df = load_data()

except Exception as e:

    st.error(
        "Unable to load cleaned dataset."
    )

    st.exception(e)

    st.stop()


# ------------------------------------------------------------
# Summary metrics
# ------------------------------------------------------------

col1, col2, col3, col4 = st.columns(4)


with col1:

    st.metric(
        "Transactions",
        f"{len(df):,}"
    )


with col2:

    st.metric(
        "Users",
        f"{df['UserId'].nunique():,}"
    )


with col3:

    st.metric(
        "Attractions",
        f"{df['AttractionId'].nunique():,}"
    )


with col4:

    st.metric(
        "Average Rating",
        f"{df['Rating'].mean():.2f}"
    )


st.divider()


# ============================================================
# Popular Attractions
# ============================================================

st.subheader(
    "🏆 Top 10 Most Visited Attractions"
)


popular_attractions = (
    df.groupby("Attraction")
    .size()
    .sort_values(
        ascending=False
    )
    .head(10)
)


st.bar_chart(
    popular_attractions
)


# ============================================================
# Top Regions
# ============================================================

st.subheader(
    "🌎 Top Regions by Visits"
)


top_regions = (
    df.groupby("Region")
    .size()
    .sort_values(
        ascending=False
    )
    .head(10)
)


st.bar_chart(
    top_regions
)


# ============================================================
# Visit Mode
# ============================================================

st.subheader(
    "👥 Visitor Mode Distribution"
)


visit_modes = (
    df["VisitMode"]
    .value_counts()
)


st.bar_chart(
    visit_modes
)


# ============================================================
# Average Rating
# ============================================================

st.subheader(
    "⭐ Top Attractions by Average Rating"
)


top_rated = (
    df.groupby("Attraction")["Rating"]
    .mean()
    .sort_values(
        ascending=False
    )
    .head(10)
)


st.bar_chart(
    top_rated
)