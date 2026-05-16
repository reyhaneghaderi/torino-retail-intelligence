from src.utils.config import PROCESSED_DIR, POSTGRES_DIR


def export_csv_outputs(
    commercial_clean,
    population_clean,
    retail_score,
    dim_quartiere,
    fact_population,
    fact_commercial_activity
):
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    POSTGRES_DIR.mkdir(parents=True, exist_ok=True)

    commercial_clean.to_csv(
        PROCESSED_DIR / "commercial_clean.csv",
        index=False
    )

    population_clean.to_csv(
        PROCESSED_DIR / "population_clean.csv",
        index=False
    )

    retail_score.to_csv(
        PROCESSED_DIR / "fact_retail_score.csv",
        index=False
    )

    dim_quartiere.to_csv(
        POSTGRES_DIR / "dim_quartiere.csv",
        index=False
    )

    fact_population.to_csv(
        POSTGRES_DIR / "fact_population.csv",
        index=False
    )

    fact_commercial_activity.to_csv(
        POSTGRES_DIR / "fact_commercial_activity.csv",
        index=False
    )

    retail_score.to_csv(
        POSTGRES_DIR / "fact_retail_score.csv",
        index=False
    )



    def export_geojson(quartieri, retail_score):
       quartieri_score = quartieri.merge(
        retail_score,
        left_on="ID_QUART",
        right_on="quartiere_id",
        how="left"
    )

    quartieri_score = quartieri_score.to_crs(epsg=4326)

    output_path = PROCESSED_DIR / "torino_quartieri_opportunity.geojson"

    quartieri_score.to_file(
        output_path,
        driver="GeoJSON"
    )

    return quartieri_score