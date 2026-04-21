from logger import get_logger

logger = get_logger("request")

def log_request(endpoint, status):
    
    logger.info(f"Endpoint: {endpoint} | Status: {status}")


if __name__ == "__main__":
    log_request("/predict", 200)
    log_request("/upload", 400)