from src.pipeline.extract import load_csv
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

import os
import sys
from dotenv import load_dotenv

logger = setup_logger(__name__)
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))

expected_schema = {
    "date":'object',
    "datetime":"datetime64[ns]",
    "cash_type":"object",
    "card":"object",
    "money":"float64",
    "coffee_name":"object",
}

validate = DataValidator(expected_schema=expected_schema)

def run_etl_pipeline():
    """
    Run the ETL pipeline to extract, transform, validate, and load data into PostgreSQL.
    """
    try:
        logger.info("Starting ETL pipeline execution...")
        
        # Step 1: Extract
        logger.info("Starting data extraction...")
        df = load_csv(os.getenv('raw_csv_path'))
        logger.info("Data extraction completed.")

        # Step 2: Transform
        logger.info("Starting data transformation...")
        df = clean_column_names(df)
        df = remove_duplicates(df)
        df = handle_missing_values(df)
        df = convert_types(df, expected_schema)
        logger.info("Data transformation completed.")

        # Step 3: Validate
        logger.info("Starting data validation...")
        validate.validate(df)
        logger.info("Data validation completed successfully.")

        # Step 4: Load
        db_handler = PostgresDBHandler(db_url=os.getenv('DB_URL'))
        db_handler.write_dataframe(df, table_name='sales_data')
        logger.info("Data loaded into PostgreSQL successfully.")

    except CustomException as ce:
        logger.error(f"ETL pipeline failed: {ce}")

if __name__ == "__main__":
 
    run_etl_pipeline()
