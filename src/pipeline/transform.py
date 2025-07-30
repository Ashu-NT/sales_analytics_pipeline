import pandas as pd
from src.logger import setup_logger

logger = setup_logger(__name__)

def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """
    Standardize column names: lowercase, replace spaces with underscores, remove special chars.
    """
    df.columns = (
        df.columns.str.strip()
                  .str.lower()
                  .str.replace(' ', '_')
                  .str.replace(r'[^\w_]', '', regex=True)
    )
    logger.info("Column names cleaned and standardized.")
    return df

def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove duplicate rows from the DataFrame.
    """
    before = len(df)
    df = df.drop_duplicates()
    after = len(df)
    logger.info(f"Removed {before - after} duplicate rows.")
    return df

def handle_missing_values(df: pd.DataFrame, strategy: str = 'drop', fill_value=None) -> pd.DataFrame:
    """
    Handle missing values in the DataFrame.
    strategy: 'drop' to remove rows, 'fill' to fill with fill_value.
    """
    nulls_before = df.isnull().sum().sum()

    if strategy == 'drop':
        df = df.dropna()
        logger.info(f"Dropped rows with missing values. ({nulls_before} nulls removed)")
    elif strategy == 'fill':
        df = df.fillna(fill_value)
        logger.info(f"Filled missing values with '{fill_value}'.")
    else:
        raise ValueError("strategy must be 'drop' or 'fill'")
    
    return df

def convert_types(df: pd.DataFrame, column_types: dict) -> pd.DataFrame:
    """
    Convert columns to specified data types.
    column_types: dict of {column_name: dtype}
    """
    for col, dtype in column_types.items():
        try:
            df[col] = df[col].astype(dtype)
            logger.info(f"🔁 Converted {col} to {dtype}")
        except Exception as e:
            logger.warning(f"Failed to convert {col} to {dtype}: {e}")
    return df
