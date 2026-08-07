import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

host=os.getenv("DB_HOST")
database=os.getenv("DB_NAME")
user=os.getenv("DB_USER")
password=os.getenv("DB_PASSWORD")

connection = psycopg2.connect(
    host=host,
    database=database,
    user=user,
    password=password
)
print("Connected to PostgreSQL successfully")