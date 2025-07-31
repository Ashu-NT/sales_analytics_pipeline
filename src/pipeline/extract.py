import pandas as pd
from src.logger import setup_logger
from dotenv import load_dotenv

logger = setup_logger(__name__)
load_dotenv()

def load_csv(file_path: str) -> pd.DataFrame:
    """
    Load a CSV file into a DataFrame.
    
    :param file_path: Path to the CSV file.
    :return: DataFrame containing the CSV data.
    """
    
    try:
        df = pd.read_csv(file_path)
        logger.info(f"CSV file loaded successfully from {file_path}.")
        return df
    except Exception as e:
        logger.error(f"Failed to load CSV file from {file_path}: {e}")
        raise
    
def save_csv(df: pd.DataFrame, file_path: str) -> None:
    """
    Save a DataFrame to a CSV file.
    
    :param df: DataFrame to save.
    :param file_path: Path where the CSV file will be saved.
    """
    
    try:
        df.to_csv(file_path, index=False)
        logger.info(f"DataFrame saved successfully to {file_path}.")
    except Exception as e:
        logger.error(f"Failed to save DataFrame to {file_path}: {e}")
        raise