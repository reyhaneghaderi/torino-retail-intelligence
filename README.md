# Turin Retail Opportunity Intelligence
## Live Demo

[Open the Streamlit App](https://torino-retail-intelligence-p96wwxmtfxkeuxptj9p5hx.streamlit.app/)
## Project Overview

This project analyzes food-service retail opportunities across the quartieri of Turin, Italy.  
The goal is to identify neighborhoods with stronger potential for cafés, bars, restaurants, and other *somministrazione* activities.
The project combines open data on commercial activities, population, metro accessibility, and neighborhood boundaries to build a retail opportunity score for each quartiere.

The final output includes:

- A Streamlit web application
- A Power BI dashboard
- A PostgreSQL data model
- Cleaned CSV datasets
- SQL scripts for table creation and analysis
## Business Problem
Opening a new food-service business requires understanding both demand and competition.  
A neighborhood with many restaurants may look attractive, but it may also be highly saturated.

This project answers the question:

> Which Turin quartieri show stronger potential for food-service retail expansion?

The analysis considers:

- Population demand
- Existing food-service competition
- Accessibility to metro stations
- Quartiere-level spatial distribution

# Data Sources
The project uses open data related to Turin, including:

- Commercial activities in Turin
- Population by quartiere
- Metro station locations
- Turin quartiere boundaries

Commercial activities were filtered to focus on *somministrazione* businesses, such as cafés, bars, and restaurants.
# Tech Stack
Python, SQL, PostgreSQL, Power BI, Streamlit
## Project Workflow

The project follows an end-to-end data analytics workflow:

1. Data collection from Turin open data sources
2. Data cleaning and standardization in Python
3. Filtering food-service activities
4. Removing duplicated commercial records
5. Spatial join between store coordinates and Turin quartieri
6. Feature engineering for demand, competition, and accessibility
7. Retail opportunity score calculation
8. PostgreSQL table creation and data loading
9. Power BI dashboard design
10. Streamlit web app deployment

## Opportunity Score Methodology

The retail opportunity score is based on three main factors:

1. **Population demand**  
   Quartieri with higher population are considered more attractive.

2. **Competition intensity**  
   Measured as the number of food-service activities per 1,000 residents.

3. **Metro accessibility**  
   Measured as the distance from each quartiere to the nearest metro station.

The final score increases with population and decreases with higher competition and longer distance from metro access.

```text
retail_opportunity_score =
0.45 × normalized_population
- 0.35 × normalized_competition
- 0.20 × normalized_distance_to_metro

 ## Opportunity levels are classified as:

Very High Opportunity
High Opportunity
Medium Opportunity
Low Opportunity
Very Low Opportunity
    
# Dashboard and Streamlit app
##Results and insights


## Folder structure
torino-retail-intelligence/
│
├── app/
│   └── streamlit_app.py
│
├── data/
│   ├── raw/
│   └── processed/
│       ├── fact_retail_score.csv
│       ├── dim_quartiere.csv
│       └── maps/
│           └── torino_quartieri_opportunity.geojson
│
├── dashboard/
│   ├── Turin_Retail_Opportunity_Dashboard.pbix
│   └── Map Analysis.pbix
│
├── docs/
│   └── data_dictionary.md
│
├── notebooks/
│   └── full project.ipynb
│
├── sql/
│   ├── 01_create_tables.sql
│   ├── 02_create_dashboard_view.sql
│   └── 03_analysis_queries.sql
│
├── src/
│   ├── extract/
│   ├── transform/
│   ├── load/
│   └── utils/
│
├── requirements.txt
├── README.md
└── LICENSE





# Future improvements
Possible improvements include:

- Adding rental price data
- Adding pedestrian traffic data
- Including income level by neighborhood
- Adding business opening and closure trends
- Comparing multiple retail categories beyond food-service activities
- Improving the map with more detailed spatial layers
- Adding predictive modeling for retail expansion potential



# Project Status
The project demonstrates skills in:

- Data cleaning
- Geospatial analysis
- SQL database modeling
- Dashboard design
- Streamlit app deployment
- End-to-end data analytics workflow
