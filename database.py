import psycopg2 #
import os 
from dotenv import load_dotenv

load_dotenv()

host=os.getenv("DB_HOST")
database=os.getenv("DB_NAME")
user=os.getenv("DB_USER")
password=os.getenv("DB_PASSWORD")
port =os.getenv("DB_PORT")

def get_connection():
    return psycopg2.connect(
        host=host,
        database=database,  
        user=user,
        password=password,
        port =port
    )

def create_transactions_table():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id SERIAL PRIMARY KEY,
            time DOUBLE PRECISION NOT NULL,
            v1 DOUBLE PRECISION NOT NULL,
            v2 DOUBLE PRECISION NOT NULL,
            v3 DOUBLE PRECISION NOT NULL,
            v4 DOUBLE PRECISION NOT NULL,
            v5 DOUBLE PRECISION NOT NULL,
            v6 DOUBLE PRECISION NOT NULL,
            v7 DOUBLE PRECISION NOT NULL,
            v8 DOUBLE PRECISION NOT NULL,
            v9 DOUBLE PRECISION NOT NULL,
            v10 DOUBLE PRECISION NOT NULL,
            v11 DOUBLE PRECISION NOT NULL,
            v12 DOUBLE PRECISION NOT NULL,
            v13 DOUBLE PRECISION NOT NULL,
            v14 DOUBLE PRECISION NOT NULL,
            v15 DOUBLE PRECISION NOT NULL,
            v16 DOUBLE PRECISION NOT NULL,
            v17 DOUBLE PRECISION NOT NULL,
            v18 DOUBLE PRECISION NOT NULL,
            v19 DOUBLE PRECISION NOT NULL,
            v20 DOUBLE PRECISION NOT NULL,
            v21 DOUBLE PRECISION NOT NULL,
            v22 DOUBLE PRECISION NOT NULL,
            v23 DOUBLE PRECISION NOT NULL,
            v24 DOUBLE PRECISION NOT NULL,
            v25 DOUBLE PRECISION NOT NULL,
            v26 DOUBLE PRECISION NOT NULL,
            v27 DOUBLE PRECISION NOT NULL,
            v28 DOUBLE PRECISION NOT NULL,
            amount DOUBLE PRECISION NOT NULL,
            fraud_score DOUBLE PRECISION NOT NULL,
            is_flagged BOOLEAN NOT NULL
        );
    """)

    connection.commit()
    cursor.close()
    connection.close()