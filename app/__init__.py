"""
This module initializes the Flask application and sets up Swagger for API documentation.
"""
from flask import Flask
from flasgger import Swagger

# Create Flask application
app = Flask(__name__)

# Setting up Swagger configuration for API documentation.
app.config['SWAGGER'] = {
    'title': 'Diabetes Predictor API',
    'description': 'This is the Diabetes Predictor API documentation.'
}
swagger = Swagger(app)

# Import log configuration and apply to the app
from config.log_config import configure_logging, log_request_info, log_response_info
configure_logging(app)
log_request_info(app)
log_response_info(app)

# Import and use the routes module
from app import routes
