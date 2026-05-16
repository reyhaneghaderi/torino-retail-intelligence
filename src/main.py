from src.extract.load_raw_data import (
    load_population,
    load_commercial_activities,
    load_metro,
    load_quartieri,
)

from src.transform.clean_data import (
    clean_population,
    clean_commercial_activities,
    clean_metro,
    clean_quartieri,
)

from src.transform.build_features import (
    filter_somministrazione,
    assign_shops_to_quartieri,
    build_dim_quartiere,
    build_fact_population,
    build_fact_commercial_activity,
    calculate_nearest_metro_distance,
)

from src.transform.build_score import build_retail_score

from src.load.export_outputs import (
    export_csv_outputs,
    export_geojson,
)


def main():
    print("1. Loading raw data...")
    pop_raw = load_population()
    com_raw = load_commercial_activities()
    metro_raw = load_metro()
    quartieri_raw = load_quartieri()

    print("2. Cleaning data...")
    pop = clean_population(pop_raw)
    com = clean_commercial_activities(com_raw)
    metro = clean_metro(metro_raw)
    quartieri = clean_quartieri(quartieri_raw)

    print("3. Filtering food-service activities...")
    som = filter_somministrazione(com)

    print("4. Assigning shops to quartieri...")
    som_with_quartiere = assign_shops_to_quartieri(som, quartieri)

    print("5. Building dimension and fact tables...")
    dim_quartiere = build_dim_quartiere(quartieri)
    fact_population = build_fact_population(pop, dim_quartiere)
    fact_commercial_activity = build_fact_commercial_activity(som_with_quartiere)

    print("6. Calculating metro distance...")
    metro_distance = calculate_nearest_metro_distance(quartieri, metro)

    print("7. Calculating retail opportunity score...")
    retail_score = build_retail_score(
        dim_quartiere=dim_quartiere,
        fact_population=fact_population,
        fact_commercial_activity=fact_commercial_activity,
        metro_distance=metro_distance,
    )

    print("8. Exporting outputs...")
    export_csv_outputs(
        commercial_clean=com,
        population_clean=pop,
        retail_score=retail_score,
        dim_quartiere=dim_quartiere,
        fact_population=fact_population,
        fact_commercial_activity=fact_commercial_activity,
    )

    export_geojson(
        quartieri=quartieri,
        retail_score=retail_score,
    )

    print("Done. Pipeline completed successfully.")


if __name__ == "__main__":
    main()