-- 01_create_tables.sql


DROP TABLE IF EXISTS fact_retail_score;
DROP TABLE IF EXISTS fact_commercial_activity;
DROP TABLE IF EXISTS fact_population;
DROP TABLE IF EXISTS dim_quartiere;

CREATE TABLE dim_quartiere (
    quartiere_id INT PRIMARY KEY,
    quartiere_name VARCHAR(100) NOT NULL,
    quartiere_name_clean VARCHAR(100)
);

CREATE TABLE fact_population (
    population_id INT PRIMARY KEY,
    quartiere_id INT NOT NULL,
    year INT,
    total_residents INT,
    male_residents INT,
    female_residents INT,

    CONSTRAINT fk_population_quartiere
        FOREIGN KEY (quartiere_id)
        REFERENCES dim_quartiere(quartiere_id)
);

CREATE TABLE fact_commercial_activity (
    activity_id INT PRIMARY KEY,
    source_commercial_activity_id VARCHAR(100),
    store_name VARCHAR(255),
    category_name VARCHAR(255),
    category_group VARCHAR(100),
    quartiere_id INT NOT NULL,
    x_coord NUMERIC(15, 3),
    y_coord NUMERIC(15, 3),
    address TEXT,

    CONSTRAINT fk_activity_quartiere
        FOREIGN KEY (quartiere_id)
        REFERENCES dim_quartiere(quartiere_id)
);

CREATE TABLE fact_retail_score (
    score_id INT PRIMARY KEY,
    quartiere_id INT NOT NULL,
    total_somministrazione INT,
    total_population INT,
    stores_per_1000_residents NUMERIC(10, 4),
    distance_to_nearest_metro NUMERIC(15, 4),
    competition_index NUMERIC(10, 4),
    normalized_population NUMERIC(10, 4),
    normalized_competition NUMERIC(10, 4),
    normalized_distance_to_metro NUMERIC(10, 4),
    retail_opportunity_score NUMERIC(10, 4),
    opportunity_level VARCHAR(50),

    CONSTRAINT fk_score_quartiere
        FOREIGN KEY (quartiere_id)
        REFERENCES dim_quartiere(quartiere_id)
);