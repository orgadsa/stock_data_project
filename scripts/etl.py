# etl.py
import pandas as pd
import os

def clean_data():
    raw_file_path = 'data/raw/stock_data.csv'
    cleaned_file_path = 'data/cleaned/cleaned_stock_data.csv'

    if not os.path.exists(raw_file_path):
        raise FileNotFoundError(f"Raw file not found: {raw_file_path}")

    df = pd.read_csv(raw_file_path)
    df['dt'] = pd.to_datetime(df['dt'], errors='coerce')
    df = df.dropna(subset=['dt'])
    df = df.sort_values(by='dt')
    df.to_csv(cleaned_file_path, index=False)
    print(f"Cleaned data saved to {cleaned_file_path}")

def transform_data():
    cleaned_file_path = 'data/cleaned/cleaned_stock_data.csv'
    transformed_file_path = 'data/transformed/transformed_stock_data.csv'

    if not os.path.exists(cleaned_file_path):
        raise FileNotFoundError(f"Cleaned file not found: {cleaned_file_path}")

    df = pd.read_csv(cleaned_file_path, parse_dates=['dt'])
    df['sp500_pct_change'] = df['sp500'].pct_change() * 100
    df['djia_pct_change'] = df['djia'].pct_change() * 100
    df.to_csv(transformed_file_path, index=False)
    print(f"Transformed data saved to {transformed_file_path}")
