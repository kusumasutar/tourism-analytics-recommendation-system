# ============================================================
# recommendation.py
#
# Contains the recommendation-system logic used by Streamlit.
# ============================================================

import pandas as pd
import numpy as np


def recommend(
    user_id,
    n,
    user_item_matrix,
    item_similarity_df,
    attraction_info
):
    """
    Generate attraction recommendations for an existing user.

    Parameters
    ----------
    user_id : int
        ID of the user.

    n : int
        Number of recommendations.

    user_item_matrix : DataFrame
        User-item ratings matrix.

    item_similarity_df : DataFrame
        Attraction similarity matrix.

    attraction_info : DataFrame
        Information about each attraction.

    Returns
    -------
    DataFrame
        Ranked attraction recommendations.
    """

    # --------------------------------------------------------
    # Check whether the user exists
    # --------------------------------------------------------

    if user_id not in user_item_matrix.index:

        return pd.DataFrame()


    # --------------------------------------------------------
    # Get ratings for this user
    # --------------------------------------------------------

    user_ratings = user_item_matrix.loc[user_id]


    # Keep only attractions the user has rated
    rated_items = user_ratings[
        user_ratings > 0
    ]


    # --------------------------------------------------------
    # If there is no rating history
    # --------------------------------------------------------

    if rated_items.empty:

        return pd.DataFrame()


    # --------------------------------------------------------
    # Calculate recommendation scores
    # --------------------------------------------------------

    scores = item_similarity_df[
        rated_items.index
    ].dot(rated_items)


    # Calculate similarity weights
    weights = item_similarity_df[
        rated_items.index
    ].sum(axis=1)


    # Prevent division by zero
    weights = weights.replace(
        0,
        np.nan
    )


    # Normalize scores
    scores = (
        scores / weights
    ).fillna(0)


    # --------------------------------------------------------
    # Don't recommend attractions already visited
    # --------------------------------------------------------

    scores = scores.drop(
        labels=rated_items.index,
        errors="ignore"
    )


    # --------------------------------------------------------
    # Select top recommendations
    # --------------------------------------------------------

    recommendations = (
        scores
        .sort_values(
            ascending=False
        )
        .head(n)
        .reset_index()
    )


    recommendations.columns = [
        "AttractionId",
        "RecommendationScore"
    ]


    # --------------------------------------------------------
    # Add attraction information
    # --------------------------------------------------------

    recommendations = recommendations.merge(
        attraction_info,
        on="AttractionId",
        how="left"
    )


    return recommendations