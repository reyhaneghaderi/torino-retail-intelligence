import pandas as pd
import geopandas as gpd

from src.utils.config import (
    POPULATION_PATH,
    COMMERCIAL_PATH,
    METRO_PATH,
    QUARTIERI_PATH,
)


def load_population():
    return pd.read_csv(POPULATION_PATH)


def load_commercial_activities():
    return pd.read_csv(COMMERCIAL_PATH, sep=";", encoding="latin-1")


def load_metro():
    return pd.read_csv(METRO_PATH)


def load_quartieri():
    return gpd.read_file(QUARTIERI_PATH)