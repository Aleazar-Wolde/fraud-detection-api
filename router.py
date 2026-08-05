from fastapi import APIRouter  
from schemas import TransactionRequest, TransactionResponse

router = APIRouter()

@router.post("/transactions", response_model=TransactionResponse)
def create_transaction(transaction: TransactionRequest):
    # Here you would typically save the transaction to a database
    # For demonstration purposes, we'll just return the transaction data
    pass

@router.get("/transactions")
def get_all_transaction():
    pass

@router.get("/transactions/flagged")
def get_flagged_transactions():
    pass

@router.get("/transactions/{id}")
def get_transaction_by_id(id: int):
    pass