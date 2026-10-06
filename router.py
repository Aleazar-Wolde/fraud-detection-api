from fastapi import APIRouter  
from schemas import TransactionRequest, TransactionResponse
from database import get_connection
import joblib

model = joblib.load("fraud_model.pkl")
scaler = joblib.load("scaler.pkl")

FRAUD_THRESHOLD = 0.1
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

    is_flagged = fraud_score >= FRAUD_THRESHOLD

    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(
        """
        INSERT INTO transactions (
            time,
            v1,
            v2,
            v3,
            v4,
            v5,
            v6,
            v7,
            v8,
            v9,
            v10,
            v11,
            v12,
            v13,
            v14,
            v15,
            v16,
            v17,
            v18,
            v19,
            v20,
            v21,
            v22,
            v23,
            v24,
            v25,
            v26,
            v27,
            v28,
            amount,
            fraud_score,
            is_flagged
        )
        VALUES (
            %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s,
            %s, %s
        )
        RETURNING id
        """,
        (
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
            transaction.amount,
            fraud_score,
            is_flagged
        )
    )

    transaction_id = cursor.fetchone()[0]

    connection.commit()

    cursor.close()
    connection.close()

    return TransactionResponse(
        id=transaction_id,
        amount=transaction.amount,
        time=transaction.time,
        v1=transaction.v1,
        v2=transaction.v2,
        v3=transaction.v3,
        v4=transaction.v4,
        v5=transaction.v5,
        v6=transaction.v6,
        v7=transaction.v7,
        v8=transaction.v8,
        v9=transaction.v9,
        v10=transaction.v10,
        v11=transaction.v11,
        v12=transaction.v12,
        v13=transaction.v13,
        v14=transaction.v14,
        v15=transaction.v15,
        v16=transaction.v16,
        v17=transaction.v17,
        v18=transaction.v18,
        v19=transaction.v19,
        v20=transaction.v20,
        v21=transaction.v21,
        v22=transaction.v22,
        v23=transaction.v23,
        v24=transaction.v24,
        v25=transaction.v25,
        v26=transaction.v26,
        v27=transaction.v27,
        v28=transaction.v28,
        fraud_score=fraud_score,
        is_flagged=is_flagged
    )


    

@router.get("/transactions")
def get_all_transaction():
    TransactionRequest
    

@router.get("/transactions/flagged")
def get_flagged_transactions():
    pass

@router.get("/transactions/{id}")
def get_transaction_by_id(id: int):
    pass