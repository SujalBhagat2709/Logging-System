import logging

def get_logger(name="app"):
    
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    
    if not logger.handlers:
        handler = logging.StreamHandler()
        
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )
        
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    
    return logger


if __name__ == "__main__":
    log = get_logger()
    log.info("Logger initialized")