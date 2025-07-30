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