# Spotify Global Chart 2024 – Data Analysis Project

## Overview
This project analyzes the Spotify Global Top 200 dataset for the year 2024 using
Exploratory Data Analysis (EDA). The objective is to understand music popularity
patterns, chart dynamics, and artist dominance on Spotify’s global charts.

The project follows the CRISP-DM framework and focuses on data cleaning,
descriptive statistics, visualization, and insight generation.
No predictive modeling or machine learning is applied.

---

## Dataset
**Spotify Global Chart 2024**

- Source: Public Spotify Global Charts dataset
- Records: 10,600 weekly observations
- Key columns:
  - Chart rank
  - Track name
  - Artist name
  - Weekly streams
  - Peak rank
  - Previous rank
  - Weeks on chart
  - New entry indicator

The dataset represents the weekly Top 200 most-streamed songs worldwide in 2024.

---

## Project Structure
spotify-top-songs/
│
├── data/
│ ├── raw/ # Original dataset
│ └── processed/ # Cleaned and transformed data
│
├── notebooks/
│ ├── 01_data_cleaning.ipynb
│ ├── 02_eda.ipynb
│ └── 03_visualizations.ipynb
│
├── reports/
│ ├── crisp_dm_report.docx
│ └── insights_summary.pdf
│
├── src/
│ ├── data_loading.py
│ ├── cleaning.py
│ ├── eda.py
│ └── plots.py
│
└── README.md


---

## Analysis Scope
**Included**
- Data cleaning and preprocessing
- Exploratory Data Analysis (EDA)
- Visualization of trends and distributions
- Business-oriented insights

**Excluded**
- Machine learning models
- Prediction or recommendation systems
- Audio feature analysis via Spotify API
- Lyrics or sentiment analysis

---

## Key Findings
- Stream counts show a strong right-skewed distribution.
- Higher-ranked songs generally achieve higher stream counts.
- A small number of artists dominate chart appearances.
- Most songs have short chart lifespans.
- New entries face strong competition to remain on the chart.

Detailed insights are available in the `insights_summary.pdf` report.

---

## Tools and Technologies
- Python
- Pandas
- Matplotlib
- Seaborn
- Jupyter Notebook

---

## Purpose
This project is intended for learning, portfolio presentation, and demonstration
of data analysis and EDA skills.