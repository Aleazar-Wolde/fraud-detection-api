# Fraud Detection API

A machine-learning-backed REST API that analyzes credit card transactions, assigns a fraud score, and flags suspicious transactions for review. The project is designed as a fraud-analysis backend, not as a payment processor.

## Architecture

```text
Client
  |
  | HTTP request
  v
FastAPI
  |
  | validates TransactionRequest
  v
StandardScaler
  |
  v
Logistic Regression model
  |
  | fraud_score + is_flagged
  v
PostgreSQL
  |
  v
TransactionResponse
```

## Tech Stack

- **Backend:** Python, FastAPI, Uvicorn
- **Machine Learning:** scikit-learn, pandas, NumPy
- **Database:** PostgreSQL, psycopg2
- **Model persistence:** joblib
- **API documentation/testing:** Swagger UI
- **Containerization:** Docker, Docker Compose
- **Planned:** AWS deployment, dashboard

## Current Status

Core backend functionality is working end-to-end.

- [x] FastAPI application and health check
- [x] Pydantic transaction request/response schemas
- [x] PostgreSQL connection using environment variables
- [x] Transaction database table
- [x] Dataset loading and preprocessing
- [x] Stratified train / validation / test split
- [x] Feature scaling with `StandardScaler`
- [x] Logistic Regression training with improved convergence
- [x] Precision, recall, and confusion-matrix evaluation
- [x] Threshold tuning using validation data
- [x] Final untouched test-set evaluation
- [x] Save and load trained model/scaler with joblib
- [x] `POST /transactions` fraud inference and database persistence
- [x] `GET /transactions`
- [x] `GET /transactions/flagged`
- [x] `GET /transactions/{id}`
- [x] 404 handling for missing transaction IDs
- [x] Structured JSON responses and FastAPI response models
- [x] End-to-end API testing through Swagger UI
- [x] Automated tests
- [x] Docker containerization
- [ ] AWS deployment
- [ ] Dashboard

## Machine Learning

The model uses Logistic Regression to estimate the probability that a transaction belongs to the fraud class.

Training flow:

```text
creditcard.csv
  -> train / validation / test split
  -> StandardScaler
  -> Logistic Regression
  -> validation threshold tuning
  -> final test evaluation
```

The selected fraud threshold is:

```text
0.1
```

Final test-set results at that threshold:

- **Precision:** ~69.6%
- **Recall:** ~79.6%
- **Confusion matrix:**

```text
[[28415    17]
 [   10    39]]
```

The validation set is used to choose the threshold. The test set is kept separate for final evaluation.

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/health` | Check API health |
| POST | `/transactions` | Analyze and store a transaction |
| GET | `/transactions` | Retrieve all stored transactions |
| GET | `/transactions/flagged` | Retrieve transactions flagged for review |
| GET | `/transactions/{id}` | Retrieve one transaction by ID |

### POST /transactions

The client sends the transaction features:

```json
{
  "amount": 149.62,
  "time": 0,
  "v1": -1.359807,
  "v2": -0.072781,
  "v3": 2.536347,
  "v4": 1.378155,
  "v5": -0.338321,
  "v6": 0.462388,
  "v7": 0.239599,
  "v8": 0.098698,
  "v9": 0.363787,
  "v10": 0.090794,
  "v11": -0.5516,
  "v12": -0.617801,
  "v13": -0.99139,
  "v14": -0.311169,
  "v15": 1.468177,
  "v16": -0.470401,
  "v17": 0.207971,
  "v18": 0.025791,
  "v19": 0.403993,
  "v20": 0.251412,
  "v21": -0.018307,
  "v22": 0.277838,
  "v23": -0.110474,
  "v24": 0.066928,
  "v25": 0.128539,
  "v26": -0.189115,
  "v27": 0.133558,
  "v28": -0.021053
}
```

The API scales the features, runs model inference, stores the transaction in PostgreSQL, and returns the generated ID with the fraud result:

```json
{
  "id": 2,
  "amount": 149.62,
  "time": 0,
  "v1": -1.359807,
  "v2": -0.072781,
  "v3": 2.536347,
  "v4": 1.378155,
  "v5": -0.338321,
  "v6": 0.462388,
  "v7": 0.239599,
  "v8": 0.098698,
  "v9": 0.363787,
  "v10": 0.090794,
  "v11": -0.5516,
  "v12": -0.617801,
  "v13": -0.99139,
  "v14": -0.311169,
  "v15": 1.468177,
  "v16": -0.470401,
  "v17": 0.207971,
  "v18": 0.025791,
  "v19": 0.403993,
  "v20": 0.251412,
  "v21": -0.018307,
  "v22": 0.277838,
  "v23": -0.110474,
  "v24": 0.066928,
  "v25": 0.128539,
  "v26": -0.189115,
  "v27": 0.133558,
  "v28": -0.021053,
  "fraud_score": 0.0005438957,
  "is_flagged": false
}
```

A flagged transaction means the model score met or exceeded the configured threshold. It is a transaction recommended for review, not confirmed fraud.

## How to Run Locally

1. Clone the repository:

```bash
git clone https://github.com/Aleazar-Wolde/fraud-detection-api.git
cd fraud-detection-api
```

2. Create and activate a virtual environment:

```bash
python -m venv .venv
```

On Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

3. Install dependencies:

```bash
python -m pip install -r requirements.txt
```

4. Create a PostgreSQL database named `fraud_detection` and add a `.env` file:

```env
DB_HOST=localhost
DB_NAME=fraud_detection
DB_USER=postgres
DB_PASSWORD=your_password
DB_PORT=5432
```

5. Download the Kaggle dataset and place it at:

```text
data/archive/creditcard.csv
```

6. Train the model and generate the saved artifacts:

```bash
python model.py
```

This creates:

```text
fraud_model.pkl
scaler.pkl
```

7. Start the API:

```bash
uvicorn main:app --reload
```

8. Open the interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

## Dataset

This project uses the [Credit Card Fraud Detection dataset](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud) from Kaggle (Machine Learning Group - ULB).

The dataset contains 284,807 transactions with 492 fraud cases, making the classification problem highly imbalanced. The `Class` column is the label and is not used as an input feature.

## Next Steps

1. Deploy the backend and database to AWS.
2. Add a lightweight fraud-review dashboard.
