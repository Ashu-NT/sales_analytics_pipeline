import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from dotenv import load_dotenv
from src.logger import setup_logger

load_dotenv()
plot_dir = os.getenv('plot_path', 'plots')

logger = setup_logger(__name__)

class SalesVisualizer:
    
    def __init__(self, plot_dir: str = None):
        self.plot_dir = plot_dir or os.getenv('plot_path', 'plots')
        os.makedirs(self.plot_dir, exist_ok=True)
         
    def plot_sales_over_time(self, df: pd.DataFrame,
                            date_col: str, 
                            sales_col: str) -> None:
        """
        Plots sales over time and saves the figure to the specified directory.
        
        Parameters:
        - df (pd.DataFrame): DataFrame containing sales data.
        - date_col (str): Column name for dates.
        - sales_col (str): Column name for sales figures.
        - output_dir (str): Directory to save the plot.
        """
        try:
           
            # Set the date column as index
            df = df.copy()
            df.set_index(date_col, inplace=True)
            
            # Plotting
            plt.figure(figsize=(12, 6))
            sns.lineplot(data=df, x=df.index, y=sales_col)
            plt.title('Sales Over Time')
            plt.xlabel('Date (YYYY-MM-DD)')
            plt.ylabel('Sales (USD)')
            plt.xticks(rotation=45)
            plt.tight_layout()
            
            # Save the plot
            output_path = os.path.join(self.plot, 'sales_over_time.png')
            plt.savefig(output_path)
            plt.close()
            
            logger.info(f"Plot saved to {output_path}")
        
        except Exception as e:
            logger.error(f"Error plotting sales over time: {e}")
            raise
        
    def plot_sales_distribution(self, df: pd.DataFrame, sales_col: str) -> None:
        """
        Plots the distribution of sales figures and saves the figure to the specified directory.
        
        Parameters:
        - df (pd.DataFrame): DataFrame containing sales data.
        - sales_col (str): Column name for sales figures.
        """
        try:
            df = df.copy()
            # Plotting
            plt.figure(figsize=(12, 6))
            sns.histplot(df[sales_col], bins=30, kde=True)
            plt.title('Sales Distribution')
            plt.xlabel('Sales (USD)')
            plt.ylabel('Frequency')
            plt.tight_layout()
            
            # Save the plot
            output_path = os.path.join(self.plot_dir, 'sales_distribution.png')
            plt.savefig(output_path)
            plt.close()
            
            logger.info(f"Plot saved to {output_path}")
        
        except Exception as e:
            logger.error(f"Error plotting sales distribution: {e}")
            raise
        
    def plot_top_products(self, df: pd.DataFrame, product_col: str, sales_col: str, top_n: int = 10) -> None:
        """
        Plots the top N products by sales and saves the figure to the specified directory.
        
        Parameters:
        - df (pd.DataFrame): DataFrame containing sales data.
        - product_col (str): Column name for product names.
        - sales_col (str): Column name for sales figures.
        - top_n (int): Number of top products to plot.
        """
        try:
            df = df.copy()
            # Get top N products by sales
            top_products = df.groupby(product_col)[sales_col].sum().nlargest(top_n).reset_index()
            
            # Plotting
            plt.figure(figsize=(12, 6))
            sns.barplot(data=top_products, x=sales_col, y=product_col)
            plt.title(f'Top {top_n} Products by Sales')
            plt.xlabel('Sales (USD)')
            plt.ylabel('Product')
            plt.tight_layout()
            
            # Save the plot
            output_path = os.path.join(self.plot_dir, 'top_products.png')
            plt.savefig(output_path)
            plt.close()
            
            logger.info(f"Plot saved to {output_path}")
        
        except Exception as e:
            logger.error(f"Error plotting top products: {e}")
            raise