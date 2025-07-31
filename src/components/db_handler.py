from sqlalchemy import create_engine, text
import pandas as pd
from src.logger import setup_logger
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))

class PostgresDBHandler:
    """
    A class to handle PostgreSQL database operations.
    """
    
    def __init__(self, db_url: str,log_file: str = None):
        self.logger = setup_logger(__name__, log_file=log_file)
        self.logger.info("Initializing PostgresDBHandler ....")
        
        if not db_url:
            db_url = os.getenv('DB_URL')
            if not db_url:
                self.logger.error("Database URL is not provided and not found in environment variables.")
                raise ValueError("Database URL must be provided or set in the environment variables.")
        
        try:
            self.engine = create_engine(db_url)
            
            with self.engine.connect() as connc:
                connc.execute(text("SELECT 1"))
            
            self.logger.info("Database connection established successfully.")
        except Exception as e:
            self.logger.error(f"Failed to connect to the database: {e}")
            raise
        
    def write_dataframe(self, df: pd.DataFrame, table_name: str, if_exists: str = 'replace') -> None:
        """
        Write a DataFrame to a PostgreSQL table.
        """
        try:
            df.to_sql(name =table_name, con = self.engine, if_exists=if_exists, index=False)
            self.logger.info(f"DataFrame written to table {table_name} (if_exists = {if_exists}).")
        except Exception as e:
            self.logger.error(f"Failed to write DataFrame to table {table_name}: {e}")
            raise
        
    def read_query(self, sql_query: str) -> pd.DataFrame:
        """
        Execute a SQL query and return the result as a DataFrame.
        """
        try:
            with self.engine.connect() as connc:
                df = pd.read_sql_query(text(sql_query), connc)
            self.logger.info(f"SQL query executed successfully: {sql_query}")
            return df
        except Exception as e:
            self.logger.error(f"Failed to execute query: {sql_query}. Error: {e}")
            raise
        
    def execute_query(self, sql_query: str) -> None:
        """
        Execute a SQL command (e.g., INSERT, UPDATE, DELETE).
        """
        try:
            with self.engine.connect() as connc:
                connc.execute(text(sql_query))
                connc.commit()
            self.logger.info(f"SQL command executed successfully: {sql_query}")
        except Exception as e:
            self.logger.error(f"Failed to execute command: {sql_query}. Error: {e}")
            raise
        
    def close(self):
        """
        Close the database connection.
        """
        try:
            self.engine.dispose()
            self.logger.info("Database connection closed successfully.")
        except Exception as e:
            self.logger.error(f"Failed to close the database connection: {e}")
            raise