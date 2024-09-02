# Diabetes-Predictor-API

## Project Description

This project provides an API to predict the risk of diabetes. The API processes input data to estimate the likelihood of having diabetes. The project is containerized using Docker and developed using the Flask framework.

## Project Structure

- **app/**: Contains application source code.
- **config/**: Contains configuration files.
- **languages/**: Contains files related to language processing.
- **logs/**: Contains application log files.
- **postman collection/**: Postman API testing collections.
- **.env**: Configuration file for environment variables.
- **Dockerfile**: Configuration file for building the Docker image.
- **README.md**: Provides information about the project.
- **requirements.txt**: Lists the Python dependencies.
- **run.py**: Python script to start the Flask application.

## Setup and Running

### Requirements

- Flask==2.2.5
- Werkzeug==2.2.3
- flasgger==0.9.7.1
- python-dotenv==0.21.0
- deep_translator==1.11.4
- numpy==1.24.3
- scikit-learn==1.4.2
- joblib==1.4.2

### Setup Using Docker

1. **Build the Docker Image**:
   ```bash
   docker build -t diabetes-predictor-api .
   ```

2. **Run the Docker Container**:
   ```bash
   docker run -d -p 5000:5000 --name diabetes-predictor-container diabetes-predictor-api
   ```

   This command will start the container in detached mode, mapping port 5000 on the host to port 5000 in the container.

3. **Verify the Container is Running**:
   ```bash
   docker ps
   ```

   This command should show the `diabetes-predictor-container` running and listening on port 5000.

4. **Test the Application**: Visit the endpoint `http://localhost:5000/health` to check if the application is running.

### Manual Setup

1. **Install Requirements**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Start the Application**:
   ```bash
   python run.py
   ```

3. **Test the Application**: Visit the endpoint `http://localhost:5000/health` to check if the application is running.

## Environment Variables

Set the necessary environment variables by editing the `.env` file. Example `.env` file:

```ini
MODEL_DIR=models
MODEL_FILENAME=best_diabetes_model.pkl
LOG_DIR=logs
LOG_FILE=app.log
```

## API Endpoints

### `/predict`
- **Method**: POST
- **Description**: Predicts if a patient has diabetes based on various medical inputs.
- **Input**: JSON object containing medical data.
- **Output**: JSON object with prediction result and probability.

Example input:
```json
{
    "Pregnancies": 6,
    "Glucose": 148,
    "BloodPressure": 72,
    "SkinThickness": 35,
    "Insulin": 30.5,
    "BMI": 33.6,
    "DiabetesPedigreeFunction": 0.627,
    "Age": 50,
    "Language": "en"
}
```

Example output:
```json
{
    "prediction": "Diabetes Detected",
    "probability": 0.75,
    "message": "Based on the provided data, there is a high likelihood of having diabetes. Please consult a healthcare professional for further evaluation."
}
```

### `/health`
- **Method**: GET
- **Description**: Health check endpoint to verify the service is running.
- **Output**: JSON object indicating service status.

Example output:
```json
{
    "status": "healthy"
}
```

## Swagger Documentation

The API includes Swagger UI for documentation and testing. You can access the Swagger UI by visiting http://localhost:5000/apidocs. Swagger provides a visual interface for interacting with the API endpoints, viewing request/response formats, and testing different scenarios.

## API Testing

Postman collections are available in the postman collection/ directory. You can import these collections into Postman to test the API endpoints.

## Logging

Application logs are stored in the logs/ directory. These logs provide detailed information about the application's operation.

## Contributing

If you would like to contribute, please create a pull request or open an issue.
