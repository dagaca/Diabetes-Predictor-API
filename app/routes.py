"""
This module contains routes for the Flask application, including
the diabetes prediction endpoint.
"""
from flask import request, jsonify
from app import app
from app.utils.prediction_utils import preprocess_input
from app.utils.model_utils import load_model
from app.utils.response_utils import generate_response

# Load the pre-trained model
model = load_model()

@app.route('/health', methods=['GET'])
def health_check():
    return "OK", 200

@app.route('/predict', methods=['POST'])
def predict():
    """
    Diabetes Predictor API
    ---
    summary: Predict if a patient has diabetes
    description: This endpoint predicts the likelihood of a patient having diabetes based on various medical inputs.
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        description: JSON object containing medical data
        required: true
        schema:
          type: object
          properties:
            Pregnancies:
              type: integer
              example: 2
            Glucose:
              type: integer
              example: 120
            BloodPressure:
              type: integer
              example: 70
            SkinThickness:
              type: integer
              example: 30
            Insulin:
              type: integer
              example: 80
            BMI:
              type: number
              example: 25.0
            DiabetesPedigreeFunction:
              type: number
              example: 0.5
            Age:
              type: integer
              example: 33
            Language:
              type: string
              example: "fr"
    responses:
      200:
        description: A successful response
        schema:
          type: object
          properties:
            prediction:
              type: string
              description: The diagnosis result (e.g., 'Diabetes Detected')
            probability:
              type: number
              description: The probability of the diagnosis
            message:
              type: string
              description: Suggestion message based on the prediction
      400:
        description: Invalid input
      500:
        description: Server error
    """
    data = request.get_json()
    app.logger.info('Received request data: %s', data)

    if not data:
        app.logger.error('No input data provided')
        return jsonify({'error': 'No input data provided'}), 400

    try:
        # Get language from request, default to 'en' if not provided
        language = data.get('Language', 'en')

        # Preprocess input
        features = preprocess_input(data)
        prediction = model.predict(features)
        probability = model.predict_proba(features)[0][1]

        # Generate response
        response = generate_response(prediction, probability, language)

        app.logger.info(
            'Prediction: %s, Probability: %s',
            response['prediction'],
            response['probability']
        )
        return jsonify(response), 200

    except KeyError as e:
        app.logger.error('Missing data: %s', str(e))
        return jsonify({'error': f'Missing data: {str(e)}'}), 400
    except ValueError as e:
        app.logger.error('Invalid data: %s', str(e))
        return jsonify({'error': f'Invalid data: {str(e)}'}), 400
    except Exception as e:
        app.logger.error('Unexpected error: %s', str(e))
        return jsonify({'error': 'An unexpected error occurred. Please try again later.'}), 500
