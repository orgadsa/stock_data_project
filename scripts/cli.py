import argparse
from scripts import etl, analysis

def main():
    parser = argparse.ArgumentParser(description="Stock Data ETL and Analysis CLI")
    subparsers = parser.add_subparsers(dest="command")

    # ETL Command
    etl_parser = subparsers.add_parser("etl", help="Run the ETL process")
    etl_parser.add_argument("--clean", action="store_true", help="Clean raw data")
    etl_parser.add_argument("--transform", action="store_true", help="Transform cleaned data")
    etl_parser.add_argument("--upload", action="store_true", help="Upload transformed data to database")

    # Analysis Command
    analysis_parser = subparsers.add_parser("analyze", help="Run data analysis and visualization")
    analysis_parser.add_argument("--correlation", action="store_true", help="Compute correlation")
    analysis_parser.add_argument("--plot", action="store_true", help="Generate time-series plots")

    args = parser.parse_args()

    if args.command == "etl":
        if args.clean:
            print("Running data cleaning...")
            etl.clean_data()
        if args.transform:
            print("Running data transformation...")
            etl.transform_data()
        if args.upload:
            print("Uploading data to database...")
            etl.upload_to_db()
    elif args.command == "analyze":
        if args.correlation:
            print("Computing correlation...")
            analysis.compute_correlation()
        if args.plot:
            print("Generating plots...")
            analysis.generate_plots()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
