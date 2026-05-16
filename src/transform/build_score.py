import pandas as pd


def minmax(series):
    denominator = series.max() - series.min()

    if denominator == 0:
        return pd.Series(0, index=series.index)

    return (series - series.min()) / denominator


def opportunity_level(score):
    if score >= 0.20:
        return "Very High Opportunity"
    elif score >= 0.05:
        return "High Opportunity"
    elif score >= -0.05:
        return "Medium Opportunity"
    elif score >= -0.15:
        return "Low Opportunity"
    else:
        return "Very Low Opportunity"


def build_retail_score(
    dim_quartiere,
    fact_population,
    fact_commercial_activity,
    metro_distance
):
    stores_by_quartiere = (
        fact_commercial_activity
        .groupby("quartiere_id")
        .size()
        .reset_index(name="n_somministrazione")
    )

    score = dim_quartiere[[
        "quartiere_id",
        "quartiere_name"
    ]].copy()

    score = score.merge(
        stores_by_quartiere,
        on="quartiere_id",
        how="left"
    )

    score["n_somministrazione"] = score["n_somministrazione"].fillna(0)

    score = score.merge(
        fact_population[["quartiere_id", "total_residents"]],
        on="quartiere_id",
        how="left"
    )

    score = score.rename(columns={
        "total_residents": "total_population"
    })

    score = score.merge(
        metro_distance,
        on="quartiere_id",
        how="left"
    )

    score["stores_per_1000_residents"] = (
        score["n_somministrazione"] / score["total_population"]
    ) * 1000

    score["competition_index"] = score["stores_per_1000_residents"]

    score["normalized_population"] = minmax(score["total_population"])
    score["normalized_competition"] = minmax(score["competition_index"])
    score["normalized_distance_to_metro"] = minmax(score["distance_to_nearest_metro"])

    score["retail_opportunity_score"] = (
        0.45 * score["normalized_population"]
        - 0.35 * score["normalized_competition"]
        - 0.20 * score["normalized_distance_to_metro"]
    )

    score["opportunity_level"] = score["retail_opportunity_score"].apply(opportunity_level)

    score.insert(0, "score_id", range(1, len(score) + 1))

    return score