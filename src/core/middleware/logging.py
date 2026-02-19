import logging
from datetime import datetime
from nexios.middleware import BaseMiddleware


class LoggingMiddleware(BaseMiddleware):
    """Middleware to log every request with method and URL using Nexios BaseMiddleware"""
    
    def __init__(self):
        super().__init__()
        # Configure logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('app.log'),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)
    
    async def process_request(self, req, res, cnext):
        """Log request before processing"""
        origin = req.headers.get("origin", "No Origin")
        self.logger.info(
            f"Request: {req.method} {req.url} - Origin: {origin}"
        )
        await cnext()
    
    async def process_response(self, req, res):
        """Log response after processing"""
        self.logger.info(
            f"Response: {req.method} {req.url} - "
            f"Status: {res.status_code}"
        )
        return res
