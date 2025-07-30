import logging
import os
from datetime import datetime

def setup_logger(name: str, log_file: str = None, level=logging.INFO) -> logging.Logger:
    """
    Setup a logger with the specified name and optional log file.
    
    :param name: Name of the logger.
    :param log_file: Optional path to the log file. If not provided, a default path will be used.
    :return: Configured logger instance.
    """
    
    logs_path = os.path.join(os.getcwd(), 'logs')
    os.makedirs(logs_path, exist_ok=True)

    if not log_file:
        log_file = os.path.join(logs_path, f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.log")
        
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    if not logger.hasHandlers():
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(level)
        
        console_handler = logging.StreamHandler()
        console_handler.setLevel(level)
        
        formatter = logging.Formatter(
            '[%(asctime)s] %(lineno)d - %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)
        
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
        
    return logger