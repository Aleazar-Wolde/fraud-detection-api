from fastapi import FastAPI
from router import router 
from database import create_transactions_table

app = FastAPI()
app.include_router(router)

@app.get("/")
def health_check():
    return {"status": "healthy"}


@app.on_event("startup")
def startup():
    create_transactions_table()