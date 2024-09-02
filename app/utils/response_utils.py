"""
This module provides utility functions for generating responses based 
on the prediction results of the diabetes prediction model.
"""
from languages.languages_operations import translate

def generate_response(prediction, probability, language='en'):
    """
    Generates a response based on the prediction and probability.
    
    Parameters:
    - prediction: Prediction result (1 or 0).
    - probability: Probability of the prediction.
    - language: The language code for the response message (default is English).
    
    Returns:
    - dict: A dictionary with a human-readable prediction and advice message.
    """
    if prediction[0] == 1:
        pred_text = "Diabetes Detected"
        message = (
            "Based on the provided data, there is a high likelihood of having diabetes. "
            "Please consult a healthcare professional for further evaluation."
        )
    else:
        pred_text = "No Diabetes Detected"
        message = (
            "Based on the provided data, there is a low likelihood of having diabetes. "
            "However, it is advisable to maintain regular health check-ups."
        )

    # Translate messages based on the selected language
    pred_text = translate(pred_text, language)
    message = translate(message, language)

    return {
        'prediction': pred_text,
        'probability': round(float(probability), 2),
        'message': message
    }
