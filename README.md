# Stock Data ETL and Analysis Project

## Overview
This project demonstrates an end-to-end ETL (Extract, Transform, Load) pipeline for stock market data. It includes data cleaning, transformation, analysis, and visualization, with functionality exposed via a Command Line Interface (CLI). The project is designed for hands-on practice with Python, `pandas`, and `matplotlib`.

## Features
- **ETL Pipeline:**
  - **Data Cleaning:** Remove duplicates, handle missing values, and validate data.
  - **Data Transformation:** Add calculated fields (e.g., percentage changes).
- **Data Analysis:**
  - Correlation analysis between time and stock indices.
  - Visualization of trends and correlations.
- **Command Line Interface:**
  - Easy interaction with the ETL and analysis functions.

## Project Structure

<!-- run etl -->
python main.py etl --clean
python main.py etl --transform
<!-- run analysis -->
python main.py analyze --correlation
python main.py analyze --plot


## Requirements
- Python 3.x
- Libraries:
  - pandas
  - matplotlib
  - seaborn

## Setup
1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd stock_data_project
2. Create venv
    python3 -m venv venv
    source venv/bin/activate
3. Install dep
    pip install -r requirements.txt

## ETL commands
1. Clean the data
    python main.py etl --clean
2. Transformed the cleam data
    python main.py etl --transform
3. Upload data to DB
    python main.py etl --upload
4. Analysis - compute correlation
    python main.py analyze --correlation
5. Generate time series plots
    python main.py analyze --plot
6. To use the SQL db
  Use the sqlite3 CLI:
  sqlite3 data/stock_data.db
  exit:
  .exit
