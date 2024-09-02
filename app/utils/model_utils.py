"""
This module contains utility functions for loading a trained model and preprocessing input data.
It is used to facilitate predictions for diabetes based on given input features.
"""
import os
from dotenv import load_dotenv
import joblib

# Load environment variables from .env file
load_dotenv()

def load_model(model_path=None):
    """
    Load the trained model from a specified file path. If no path is provided, it defaults to
    'best_diabetes_model.pkl' located in the 'models' directory under the base directory.

    Parameters:
    - model_path (str): The path to the model file. If None, the default path is used.

    Returns:
    - model: The loaded machine learning model.

    Raises:
    - FileNotFoundError: If the specified model file does not exist.
    """
    if model_path is None:
        # Correctly find the path to the 'models' directory,
        # which is at the same level as the 'app' directory
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # Read the model directory and filename from environment variables
        model_dir = os.getenv('MODEL_DIR')
        model_filename = os.getenv('MODEL_FILENAME')
        # Construct the model path
        model_path = os.path.join(base_dir, model_dir, model_filename)

    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found: {model_path}")

    return joblib.load(model_path)
