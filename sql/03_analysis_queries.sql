-- 03_analysis_queries.sql

-- Check number of rows in each table
SELECT COUNT(*) AS n_quartieri
FROM dim_quartiere;

SELECT COUNT(*) AS n_population_records
FROM fact_population;

SELECT COUNT(*) AS n_commercial_activities
FROM fact_commercial_activity;

SELECT COUNT(*) AS n_retail_score_records
FROM fact_retail_score;


-- Count somministrazione activities by quartiere
SELECT
    q.quartiere_id,
    q.quartiere_name,
    COUNT(a.activity_id) AS n_somministrazione
FROM dim_quartiere q
LEFT JOIN fact_commercial_activity a
    ON q.quartiere_id = a.quartiere_id
GROUP BY
    q.quartiere_id,
    q.quartiere_name
ORDER BY
    n_somministrazione DESC;


-- Final retail opportunity ranking
SELECT
    q.quartiere_id,
    q.quartiere_name,
    s.total_somministrazione,
    s.total_population,
    s.stores_per_1000_residents,
    s.distance_to_nearest_metro,
    s.retail_opportunity_score,
    s.opportunity_level
FROM fact_retail_score s
JOIN dim_quartiere q
    ON s.quartiere_id = q.quartiere_id
ORDER BY
    s.retail_opportunity_score DESC;


-- Power BI dashboard view output
SELECT *
FROM vw_retail_opportunity_dashboard
ORDER BY retail_opportunity_score DESC;