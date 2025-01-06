# analysis.py
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

def compute_correlation():
    transformed_file_path = 'data/transformed/transformed_stock_data.csv'
    df = pd.read_csv(transformed_file_path, parse_dates=['dt'], index_col='dt')

    df['time_numeric'] = (df.index - df.index[0]).days
    correlation = df[['time_numeric', 'sp500', 'djia', 'hsi']].corr()
    print("\nCorrelation Matrix:")
    print(correlation)

    output_plots_path = 'outputs/plots'
    os.makedirs(output_plots_path, exist_ok=True)

    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Correlation Heatmap')
    heatmap_path = os.path.join(output_plots_path, 'correlation_heatmap.png')
    plt.savefig(heatmap_path)
    plt.close()
    print(f"Correlation heatmap saved to {heatmap_path}")

def generate_plots():
    transformed_file_path = 'data/transformed/transformed_stock_data.csv'
    df = pd.read_csv(transformed_file_path, parse_dates=['dt'], index_col='dt')

    output_plots_path = 'outputs/plots'
    os.makedirs(output_plots_path, exist_ok=True)

    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df['sp500'], label='S&P 500', color='blue')
    plt.plot(df.index, df['djia'], label='DJIA', color='green')
    plt.plot(df.index, df['hsi'], label='HSI', color='red')
    plt.title('Index Prices Over Time')
    plt.xlabel('Date')
    plt.ylabel('Index Price')
    plt.legend()
    plot_path = os.path.join(output_plots_path, 'index_prices_over_time.png')
    plt.savefig(plot_path)
    plt.close()
    print(f"Time-series plots saved to {plot_path}")
