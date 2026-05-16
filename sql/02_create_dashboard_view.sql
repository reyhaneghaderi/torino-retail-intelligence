-- 02_create_dashboard_view.sql


DROP VIEW IF EXISTS vw_retail_opportunity_dashboard;

CREATE VIEW vw_retail_opportunity_dashboard AS
SELECT
    q.quartiere_id,
    q.quartiere_name,
    s.total_somministrazione,
    s.total_population,
    s.stores_per_1000_residents,
    s.distance_to_nearest_metro,
    s.competition_index,
    s.normalized_population,
    s.normalized_competition,
    s.normalized_distance_to_metro,
    s.retail_opportunity_score,
    s.opportunity_level
FROM fact_retail_score s
JOIN dim_quartiere q
    ON s.quartiere_id = q.quartiere_id;