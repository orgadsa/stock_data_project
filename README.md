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

## Commands
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
   
## Continuous Integration (CI)
This project uses GitHub Actions for Continuous Integration to ensure code quality and reliability. The CI workflow is triggered on every push to the main branch or on pull requests. It performs the following steps:

### CI Workflow Overview
Environment Setup:

The workflow runs on ubuntu-latest.
It tests the code on multiple Python versions (3.8, 3.9, and 3.10).
Steps Performed:

Checkout Code: Fetches the latest version of the code from the repository.
Set Up Python: Installs the specified Python version using the setup-python action.
Install Dependencies: Installs all required dependencies from requirements.txt.
Run Unit Tests:
Executes tests located in the tests/ directory using pytest.
Ensures all tests pass successfully before proceeding.
Code Style Check with Flake8:
Lints the codebase to ensure adherence to Python coding standards.
Code Formatting Check with Black:
Verifies that the codebase is properly formatted according to Black.
Debugging:

If errors occur, the workflow logs can be reviewed to identify issues. You can also add a Debug - List files step in the workflow to verify the file structure during CI runs.
