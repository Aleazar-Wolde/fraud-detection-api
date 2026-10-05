from fastapi import APIRouter  
from schemas import TransactionRequest, TransactionResponse
from database import get_connection
import joblib

model = joblib.load("fraud_model.pkl")
scaler = joblib.load("scaler.pkl")

FREAD_THRESHOLD = 0.1
router = APIRouter()

@router.post("/transactions", response_model=TransactionResponse)
def create_transaction(transaction: TransactionRequest):
    transaction_features = [[
        transaction.time,
        transaction.v1,
        transaction.v2,
        transaction.v3,
        transaction.v4,
        transaction.v5,
        transaction.v6,
        transaction.v7,
        transaction.v8,
        transaction.v9,
        transaction.v10,
        transaction.v11,
        transaction.v12,
        transaction.v13,
        transaction.v14,
        transaction.v15,
        transaction.v16,
        transaction.v17,
        transaction.v18,
        transaction.v19,
        transaction.v20,
        transaction.v21,
        transaction.v22,
        transaction.v23,
        transaction.v24,
        transaction.v25,
        transaction.v26,
        transaction.v27,
        transaction.v28,
        transaction.amount
    ]]
    scaled_transaction = scaler.transform(transaction_features)
    probabilities = model.predict_proba(scaled_transaction)
    fraud_score = float(probabilities[0][1])
    is_flagged = fraud_score >= FREAD_THRESHOLD
    connection = get_connection()
    cursor = connection.cursor()

@router.get("/transactions")
def get_all_transaction():
    TransactionRequest
    

@router.get("/transactions/flagged")
def get_flagged_transactions():
    pass

@router.get("/transactions/{id}")
def get_transaction_by_id(id: int):
    pass