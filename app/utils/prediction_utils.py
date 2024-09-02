"""
This module provides utility functions for preprocessing input data
for the diabetes prediction model.
"""
import numpy as np
from sklearn.preprocessing import StandardScaler, PolynomialFeatures

def preprocess_input(data):
    """
    Preprocess input data to match the expected input format of the model.

    Parameters:
    - data (dict): Input data containing the original 8 features.

    Returns:
    - np.array: Processed feature array with the same number of features 
                used in model training (42 features).
    """
    # Extract original features from JSON input
    original_features = [
        data['Pregnancies'],
        data['Glucose'],
        data['BloodPressure'],
        data['SkinThickness'],
        data['Insulin'],
        data['BMI'],
        data['DiabetesPedigreeFunction'],
        data['Age']
    ]

    # Convert to numpy array and reshape
    original_features_array = np.array(original_features).reshape(1, -1)

    # Feature Scaling (use the same scaler as used during training)
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(original_features_array)

    # Create polynomial features to capture interactions
    poly = PolynomialFeatures(degree=2, interaction_only=True, include_bias=False)
    X_poly = poly.fit_transform(scaled_features)

    # Generate additional statistical features
    bmi_squared = data['BMI'] ** 2
    age_glucose_interaction = data['Age'] * data['Glucose']
    insulin_skinthickness_ratio = data['Insulin'] / (data['SkinThickness'] + 1)
    glucose_bmi_interaction = data['Glucose'] * data['BMI']
    age_insulin_interaction = data['Age'] * data['Insulin']
    pregnancies_glucose_interaction = data['Pregnancies'] * data['Glucose']

    # Combine all features
    additional_features = np.array([
        bmi_squared,
        age_glucose_interaction,
        insulin_skinthickness_ratio,
        glucose_bmi_interaction,
        age_insulin_interaction,
        pregnancies_glucose_interaction
    ]).reshape(1, -1)

    # Stack all features together to form the final feature set
    all_features = np.hstack([X_poly, additional_features])

    # Ensure the result is exactly 42 features
    if all_features.shape[1] != 42:
        raise ValueError(
            f"Processed features have {all_features.shape[1]} features, "
            f"expected 42 features."
        )
    return all_features
