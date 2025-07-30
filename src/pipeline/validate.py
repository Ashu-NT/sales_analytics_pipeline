import pandas as pd
from src.logger import setup_logger

logger = setup_logger(__name__)

class DataValidator:
    
    def __init__(self, expected_columns: dict, null_threshold: float = 0.1):
        """
        Initialize the DataValidator with expected columns and null threshold.
        
        :param expected_columns: Dictionary with table names as keys and list of expected columns as values.
        :param null_threshold: Maximum allowed percentage (10%) of null values in a column.
        """
        self.expected_columns = expected_columns
        self.null_threshold = null_threshold
    
    def validate_schema(self, df: pd.DataFrame):
        """
        Validate the schema of the DataFrame against expected columns.
        
        :param df: DataFrame to validate.
        :param table_name: Name of the table for which the schema is being validated.
        :return: True if schema is valid, False otherwise.
        """
        
        logger.info("Validating schema...")
        
        missing_columns = set(self.expected_columns.keys()) - set(df.columns)
        if missing_columns:
            logger.error(f"Missing columns: {missing_columns}")
            raise ValueError(f"Missing columns: {missing_columns}")
        
        for col, dtype in self.expected_columns.items():
            if not pd.api.types.is_dtype_equal(df[col].dtype, dtype):
                logger.warning(f"Column {col} has incorrect type: expected {dtype}, got {df[col].dtype}")

    logger.info("Schema validation passed.")
    
    def validate_nulls(self, df: pd.DataFrame):
        """
        Validate the percentage of null values in each column.
        
        :param df: DataFrame to validate.
        :return: True if null validation passes, False otherwise.
        """
        
        logger.info("Validating null values...")
        
        null_counts = df.isnull().mean()
        high_null_columns = null_counts[null_counts > self.null_threshold]
        
        if not high_null_columns.empty:
            logger.warning(f"Columns with high null values: {high_null_columns}")

        else:
            logger.info("No columns exceed the null threshold.")
        
        logger.info("Null value validation passed.")
        
    def validate(self, df: pd.DataFrame):
        """
        Validate the DataFrame by checking schema and null values.
        
        :param df: DataFrame to validate.
        :return: True if all validations pass, False otherwise.
        """
        logger.info("Starting full data validation...")
         
        try:
            self.validate_schema(df)
            self.validate_nulls(df)
            logger.info("Data validation passed.")
        
        except Exception as e:
            logger.error(f"Data validation failed: {e}")