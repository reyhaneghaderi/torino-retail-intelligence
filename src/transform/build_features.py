def filter_somministrazione(com):
    som = com[com["category_group"] == "somministrazione"].copy()

    dup_keys = [
        "address_clean",
        "category_group",
        "x",
        "y",
    ]

    som = som.drop_duplicates(subset=dup_keys, keep="first")
    som = som.dropna(subset=["x", "y"])

    return som

import geopandas as gpd
import numpy as np 


def assign_shops_to_quartieri(som, quartieri):
    som_gdf = gpd.GeoDataFrame(
        som.copy(),
        geometry=gpd.points_from_xy(som["x"], som["y"]),
        crs="EPSG:3003"
    )

    if som_gdf.crs != quartieri.crs:
        som_gdf = som_gdf.to_crs(quartieri.crs)

    som_with_quartiere = gpd.sjoin(
        som_gdf,
        quartieri[["ID_QUART", "DENOM", "geometry"]],
        how="left",
        predicate="within"
    )

    return som_with_quartiere

def build_dim_quartiere(quartieri):
    dim_quartiere = quartieri[[
        "ID_QUART",
        "DENOM",
        "quartiere_name_clean",
    ]].copy()

    dim_quartiere = dim_quartiere.rename(columns={
        "ID_QUART": "quartiere_id",
        "DENOM": "quartiere_name",
    })

    return dim_quartiere


from src.utils.config import YEAR


def build_fact_population(pop, dim_quartiere):
    fact_population = pop.merge(
        dim_quartiere,
        on="quartiere_name_clean",
        how="left"
    )

    fact_population = fact_population[[
        "quartiere_id",
        "total_population",
        "male",
        "female",
    ]].copy()

    fact_population = fact_population.rename(columns={
        "total_population": "total_residents",
        "male": "male_residents",
        "female": "female_residents",
    })

    fact_population["year"] = YEAR
    fact_population.insert(0, "population_id", range(1, len(fact_population) + 1))

    return fact_population

def build_fact_commercial_activity(som_with_quartiere):
    fact = som_with_quartiere.copy()

    fact = fact.rename(columns={
        "ID_QUART": "quartiere_id",
        "commercial_activity_id": "source_commercial_activity_id",
        "shop_sign_name": "store_name",
        "category": "category_name",
        "x": "x_coord",
        "y": "y_coord",
    })

    fact = fact[[
        "source_commercial_activity_id",
        "store_name",
        "category_name",
        "category_group",
        "quartiere_id",
        "x_coord",
        "y_coord",
        "address",
    ]].copy()

    fact.insert(0, "activity_id", range(1, len(fact) + 1))

    return fact


    


def calculate_nearest_metro_distance(quartieri, metro):
    quartieri_3003 = quartieri.to_crs("EPSG:3003").copy()

    quartieri_3003["centroid"] = quartieri_3003.geometry.centroid
    quartieri_3003["centroid_x"] = quartieri_3003["centroid"].x
    quartieri_3003["centroid_y"] = quartieri_3003["centroid"].y

    def nearest_distance(row):
        distances = np.sqrt(
            (metro["x"] - row["centroid_x"]) ** 2 +
            (metro["y"] - row["centroid_y"]) ** 2
        )
        return distances.min()

    quartieri_3003["distance_to_nearest_metro"] = quartieri_3003.apply(
        nearest_distance,
        axis=1
    )

    metro_distance = quartieri_3003[[
        "ID_QUART",
        "distance_to_nearest_metro"
    ]].copy()

    metro_distance = metro_distance.rename(columns={
        "ID_QUART": "quartiere_id"
    })

    return metro_distance