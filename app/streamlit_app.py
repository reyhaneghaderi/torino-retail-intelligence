from pathlib import Path
import json

import streamlit as st
import pandas as pd
import plotly.express as px


# -----------------------------
# Page config
# -----------------------------
st.set_page_config(
    page_title="Turin Retail Opportunity",
    layout="wide"
)

st.title("Turin Food-Service Retail Opportunity App")
st.markdown(
    "Identifying Turin quartieri with stronger potential for cafés, bars, and restaurant expansion."
)


# -----------------------------
# Load data
# -----------------------------
@st.cache_data
def load_data():
    base_dir = Path(__file__).resolve().parents[1]

    score_path = base_dir / "data" / "processed" / "fact_retail_score.csv"
    dim_path = base_dir / "data" / "processed" / "dim_quartiere.csv"
    geojson_path = (
        base_dir
        / "data"
        / "processed"
        / "maps"
        / "torino_quartieri_opportunity.geojson"
    )

    score = pd.read_csv(score_path)
    dim_quartiere = pd.read_csv(dim_path)

    with open(geojson_path, "r", encoding="utf-8") as f:
        geojson = json.load(f)

    score["quartiere_id"] = score["quartiere_id"].astype(int)
    dim_quartiere["quartiere_id"] = dim_quartiere["quartiere_id"].astype(int)

    # Add quartiere_name from dim_quartiere
    score = score.merge(
        dim_quartiere[["quartiere_id", "quartiere_name"]],
        on="quartiere_id",
        how="left"
    )

    # If some names are missing, create fallback names
    score["quartiere_name"] = score["quartiere_name"].fillna(
        "Quartiere " + score["quartiere_id"].astype(str)
    )

    # Create opportunity_level if missing
    if "opportunity_level" not in score.columns:
        def classify_opportunity(x):
            if x >= 0.20:
                return "Very High Opportunity"
            elif x >= 0.05:
                return "High Opportunity"
            elif x >= -0.05:
                return "Medium Opportunity"
            elif x >= -0.15:
                return "Low Opportunity"
            else:
                return "Very Low Opportunity"

        score["opportunity_level"] = score["retail_opportunity_score"].apply(
            classify_opportunity
        )

    return score, geojson


score, geojson = load_data()


# -----------------------------
# Colors
# -----------------------------
level_colors = {
    "Very High Opportunity": "#1b5e20",
    "High Opportunity": "#66bb6a",
    "Medium Opportunity": "#fbc02d",
    "Low Opportunity": "#e57373",
    "Very Low Opportunity": "#d73027"
}

level_order = [
    "Very High Opportunity",
    "High Opportunity",
    "Medium Opportunity",
    "Low Opportunity",
    "Very Low Opportunity"
]


# -----------------------------
# Sidebar filters
# -----------------------------
st.sidebar.header("Filters")

available_levels = [
    level for level in level_order
    if level in score["opportunity_level"].dropna().unique()
]

selected_levels = st.sidebar.multiselect(
    "Opportunity level",
    options=available_levels,
    default=available_levels
)

filtered_score = score[
    score["opportunity_level"].isin(selected_levels)
].copy()


# -----------------------------
# KPI cards
# -----------------------------
total_activities = int(filtered_score["total_somministrazione"].sum())
total_population = int(filtered_score["total_population"].sum())
avg_stores = filtered_score["stores_per_1000_residents"].mean()

col1, col2, col3 = st.columns(3)

col1.metric("Food-Service Activities", f"{total_activities:,}")
col2.metric("Total Population", f"{total_population:,}")
col3.metric("Avg Stores per 1,000 Residents", f"{avg_stores:.2f}")

st.divider()


# -----------------------------
# Tabs
# -----------------------------
tab1, tab2 = st.tabs(["Overview Dashboard", "Map Analysis"])


# =====================================================
# TAB 1 — OVERVIEW DASHBOARD
# =====================================================
with tab1:
    st.header("Overview Dashboard")
    st.markdown(
        "Summary of food-service activity, population, competition, and opportunity score by quartiere."
    )

    left_col, right_col = st.columns([1.1, 1])

    with left_col:
        st.subheader("Retail Opportunity Score by Quartiere")

        chart_data = filtered_score.sort_values(
            "retail_opportunity_score",
            ascending=True
        )

        fig_bar = px.bar(
            chart_data,
            x="retail_opportunity_score",
            y="quartiere_name",
            color="opportunity_level",
            color_discrete_map=level_colors,
            orientation="h",
            hover_data=[
                "total_somministrazione",
                "total_population",
                "stores_per_1000_residents",
                "distance_to_nearest_metro"
            ]
        )

        fig_bar.update_layout(
            height=650,
            xaxis_title="Retail Opportunity Score",
            yaxis_title="Quartiere",
            legend_title="Opportunity Level",
            margin={"r": 10, "t": 10, "l": 10, "b": 10}
        )

        st.plotly_chart(fig_bar, use_container_width=True)

    with right_col:
        st.subheader("Quartiere-Level Details")

        display_cols = [
            "quartiere_name",
            "total_somministrazione",
            "total_population",
            "stores_per_1000_residents",
            "distance_to_nearest_metro",
            "retail_opportunity_score",
            "opportunity_level"
        ]

        table_data = filtered_score[display_cols].sort_values(
            "retail_opportunity_score",
            ascending=False
        )

        st.dataframe(
            table_data,
            use_container_width=True,
            height=650
        )


# =====================================================
# TAB 2 — MAP ANALYSIS
# =====================================================
with tab2:
    st.header("Opportunity Map")
    st.markdown(
        "Green quartieri indicate stronger opportunity. Red quartieri indicate weaker opportunity."
    )

    map_data = filtered_score.copy()

    fig_map = px.choropleth_mapbox(
        map_data,
        geojson=geojson,
        locations="quartiere_id",
        featureidkey="properties.ID_QUART",
        color="opportunity_level",
        color_discrete_map=level_colors,
        hover_name="quartiere_name",
        hover_data={
            "opportunity_level": True,
            "total_somministrazione": True,
            "total_population": True,
            "stores_per_1000_residents": ":.2f",
            "distance_to_nearest_metro": ":.0f",
            "retail_opportunity_score": ":.3f",
            "quartiere_id": False
        },
        mapbox_style="carto-positron",
        center={"lat": 45.0703, "lon": 7.6869},
        zoom=10.2,
        opacity=0.75
    )

    fig_map.update_layout(
        height=750,
        margin={"r": 0, "t": 0, "l": 0, "b": 0},
        legend_title_text="Opportunity Level"
    )

    st.plotly_chart(fig_map, use_container_width=True)

    st.subheader("Interpretation")
    st.markdown(
        """
        The map shows opportunity levels across Turin quartieri.
        The score combines population demand, local competition, and metro accessibility.
        Higher scores indicate stronger potential for food-service expansion.
        """
    )
    