# TMDB Movie Data Pipeline

## 📌 Project Overview
This project is an end-to-end data pipeline built using the TMDB API.
The pipeline extracts movie metadata, applies data transformations and feature engineering,
and loads the processed data into a PostgreSQL database for analysis.

## 🛠️ Tech Stack
- Python
- TMDB API
- Pandas
- PostgreSQL
- Apache Airflow
- Docker

## 🔄 Pipeline Architecture
1. Extract movie data from TMDB API
2. Transform data (cleaning, feature engineering, normalization)
3. Load transformed data into PostgreSQL

TMDB API → Extract → Transform → Load → PostgreSQL

## 🔧 Data Transformations
- Converted release dates to datetime format
- Normalized popularity scores
- Applied IMDb-style weighted rating
- Exploded genre lists into relational tables
- Performed sentiment analysis on movie overviews


## 📁 Project Structure
tmdb_pipeline/
│
├── dags/
│   └── tmdb_dag.py
├── scripts/
│   ├── extract.py
│   ├── transform.py
│   └── load.py
├── requirements.txt
└── README.md



