# Fraud Detection API

A backend system that analyzes credit card transactions and flags 
potentially fraudulent ones for review. Built as a machine learning-backed 
REST API — not a payment processor — designed to help a fraud analyst 
quickly identify suspicious transactions instead of manually reviewing 
every one.

## Tech Stack

- **Backend:** Python, FastAPI
- **Machine Learning:** scikit-learn
- **Database:** PostgreSQL
- **Containerization:** Docker
- **Deployment:** AWS
- **Dashboard:** React or HTML

## Current Status

This project is actively in development. Progress so far:

- [x] FastAPI app skeleton with health check endpoint
- [x] Transaction request/response schemas (Pydantic)
- [x] All 4 API endpoint routes defined
- [x] PostgreSQL database connection configured
- [x] Dataset loading and preprocessing
- [x] Train / validation / test split
- [x] Logistic Regression model training
- [x] Precision, recall, and confusion matrix evaluation
- [x] Threshold tuning using validation data
- [x] Final test-set evaluation
- [ ] Feature scaling and convergence improvement
- [ ] Save trained model for API inference
- [ ] Endpoint logic implementation
- [ ] Docker containerization
- [ ] AWS deployment
- [ ] Dashboard

## ML Training Notes

- Each feature has its own learned coefficient (weight).
- The same coefficient for a feature is shared across all training transactions.
- During training, Logistic Regression adjusts coefficients and the intercept to reduce loss.
- The current model reaches the default `max_iter=100` before convergence.
- The next step is to apply feature scaling with `StandardScaler` and retrain the model.

## How to Run Locally

1. Clone the repository:

git clone https://github.com/Aleazar-Wolde/fraud-detection-api.git
cd fraud-detection-api


2. Install dependencies:

pip install -r requirements.txt


3. Set up a PostgreSQL database and create a `.env` file with:

DB_HOST=localhost
DB_NAME=fraud_detection
DB_USER=your_username
DB_PASSWORD=your_password


4. Run the server:

uvicorn main:app --reload


5. Visit `http://127.0.0.1:8000/docs` to see the interactive API documentation.

## API Endpoints

| Method | Endpoint                  | Description                          |
|--------|----------------------------|---------------------------------------|
| GET    | `/health`                  | Health check                          |
| POST   | `/transactions`            | Submit a transaction for analysis     |
| GET    | `/transactions`            | Retrieve all transactions             |
| GET    | `/transactions/flagged`    | Retrieve only flagged transactions    |
| GET    | `/transactions/{id}`       | Retrieve a specific transaction by ID |

## Dataset

This project uses the [Credit Card Fraud Detection dataset](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud) 
from Kaggle (Machine Learning Group - ULB). Download `creditcard.csv` 
and place it in a `data/` folder in the project root before training the model.