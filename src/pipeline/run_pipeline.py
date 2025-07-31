from src.pipeline.extract import load_csv, save_csv
from src.pipeline.transform import (
    clean_column_names,
    remove_duplicates,
    handle_missing_values,
    convert_types
)

from src.pipeline.validate import DataValidator
from src.components.db_handler import PostgresDBHandler
from src.logger import setup_logger
from src.components.exception import CustomException
from src.config import expected_schema
from src.components.visualizer import SalesVisualizer

import os
from dotenv import load_dotenv

logger = setup_logger(__name__)
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))

validate = DataValidator(expected_columns=expected_schema)
visualizer = SalesVisualizer()  

def run_etl_pipeline():
    """
    Run the ETL pipeline to extract, transform, validate, and load data into PostgreSQL.
    """
    try:
        logger.info("Starting ETL pipeline execution...")
        
        # Extract
        logger.info("Starting data extraction...")
        df = load_csv(os.getenv('raw_csv_path'))
        logger.info("Data extraction completed.")

        # Transform
        logger.info("Starting data transformation...")
        df = clean_column_names(df)
        df = remove_duplicates(df)
        df = handle_missing_values(df)
        df = convert_types(df, expected_schema)
        logger.info("Data transformation completed.")
        
        # Save transformed data to CSV 
        save_csv(df, os.getenv('processed_csv_path'))
        logger.info(f"Transformed data saved to {os.getenv('processed_csv_path')}.")
        
        # Validate
        logger.info("Starting data validation...")
        df_transform = load_csv(os.getenv('processed_csv_path'))
        validate.validate(df_transform)
        logger.info("Data validation completed successfully.")
        
        # Visualize 
        visualizer.plot_sales_over_time(df_transform, date_col='datetime', sales_col='money')
        visualizer.plot_sales_distribution(df_transform, sales_col='money')     
        visualizer.plot_top_products(df_transform, product_col='coffee_name', sales_col='money', top_n=10)

        # Load to PostgreSQL
        db_handler = PostgresDBHandler(db_url=os.getenv('DB_URL'))
        db_handler.write_dataframe(df_transform, table_name='sales_data')
        logger.info("Data loaded into PostgreSQL successfully.")

    except CustomException as ce:
        logger.error(f"ETL pipeline failed: {ce}")

if __name__ == "__main__":
 
    run_etl_pipeline()
