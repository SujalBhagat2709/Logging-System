import logging

def get_file_logger(name="file_logger", file_name="app.log"):
    
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    
    if not logger.handlers:
        file_handler = logging.FileHandler(file_name)
        
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )
        
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    
    return logger


if __name__ == "__main__":
    log = get_file_logger()
    log.info("This is saved in file")