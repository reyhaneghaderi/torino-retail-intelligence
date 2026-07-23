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

The retail opportunity score combines three factors:

1. **Population demand**  
   Quartieri with a larger population receive a higher demand score.

2. **Competition intensity**  
   Competition is measured using the number of food-service businesses per 1,000 residents.

3. **Metro accessibility**  
   Accessibility is measured using the distance to the nearest metro station.

The final score is calculated as:

```text
Retail Opportunity Score =
    0.45 × Normalized Population
  - 0.35 × Normalized Competition
  - 0.20 × Normalized Distance to Metro
```

A higher score represents stronger estimated potential for food-service retail expansion.

### Opportunity Levels

The final scores are grouped into five categories:

- Very High Opportunity
- High Opportunity
- Medium Opportunity
- Low Opportunity
- Very Low Opportunity

## Dashboard and Streamlit Application

The project includes two interfaces:

- A **Streamlit application** for interactive map exploration and quartiere comparison
- A **Power BI dashboard** for business-level reporting and visual analysis

[Open the live Streamlit application](https://torino-retail-intelligence-p96wwxmtfxkeuxptj9p5hx.streamlit.app)

## Results and Insights

The analysis produces:

- A retail opportunity score for every quartiere
- Competition density per 1,000 residents
- Population-demand indicators
- Distance-to-metro indicators
- Opportunity-level classifications
- An interactive geospatial map

The model should be interpreted as a decision-support tool rather than a guarantee of business success. Rental costs, pedestrian traffic, household income and commercial-property availability are not currently included.

## Project Structure

```text
torino-retail-intelligence/
│
├── app/
│   └── streamlit_app.py
│
├── dashboard/
│   ├── Turin_Retail_Opportunity_Dashboard.pbix
│   └── Map Analysis.pbix
│
├── data/
│   ├── raw/
│   └── processed/
│       ├── fact_retail_score.csv
│       ├── dim_quartiere.csv
│       └── maps/
│           └── torino_quartieri_opportunity.geojson
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
```

## Run the Project Locally

Clone the repository:

```bash
git clone https://github.com/reyhaneghaderi/torino-retail-intelligence.git
cd torino-retail-intelligence
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Start the Streamlit application:

```bash
streamlit run app/streamlit_app.py
```

## Data Sources

The project uses open data related to Turin:

- Commercial activities on private premises
- Population by sex and quartiere
- Turin metro station locations
- Quartiere geographic boundaries

Commercial activities were filtered to focus on food-service businesses classified as `somministrazione`.

## Limitations

The opportunity score is based on available public data and a manually defined weighting system.

Current limitations include:

- No commercial rental-price information
- No pedestrian-footfall data
- No household-income information
- No historical business opening and closure data
- Metro access is only one component of overall accessibility
- The score has not been validated against actual business profitability

## Future Improvements

Possible improvements include:

- Adding commercial rental-price data
- Adding pedestrian-traffic information
- Including income indicators by quartiere
- Analysing business openings and closures over time
- Comparing different types of retail activities
- Testing alternative score weights
- Adding sensitivity analysis
- Adding predictive modelling when sufficient historical data becomes available

## Skills Demonstrated

- Python data cleaning and transformation
- Geospatial data analysis
- Feature engineering
- PostgreSQL database modelling
- SQL analysis
- Power BI dashboard development
- Streamlit application deployment
- Business-oriented analytical reporting


