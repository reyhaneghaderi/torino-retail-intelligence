from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]

DATA_DIR = BASE_DIR / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"
POSTGRES_DIR = PROCESSED_DIR / "postgresql"

POPULATION_PATH = RAW_DIR / "A2_Pop_per_Sesso_e_Quartiere.csv"
COMMERCIAL_PATH = RAW_DIR / "attivita_commerciali.csv"
METRO_PATH = RAW_DIR / "fermate_linee_metro.csv"
QUARTIERI_PATH = RAW_DIR / "quartieri_shapefile" / "ex_neighborhood_boundary.shp"

YEAR = 2023