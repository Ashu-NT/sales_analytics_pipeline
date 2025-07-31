from src.pipeline.run_pipeline import run_etl_pipeline
from src.logger import setup_logger

if __name__ == "__main__":
    logger = setup_logger(__name__)
    try:
        run_etl_pipeline()
        logger.info("ETL pipeline executed successfully.")
    except Exception as e:
        logger.error(f"ETL pipeline execution failed: {e}")
        raise