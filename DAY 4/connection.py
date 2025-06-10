import pymysql
import logging
from dotenv import load_dotenv
import os

load_dotenv()

logging.basicConfig(
    filename="Trigger_logs.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def get_connection():
    try:
        conn = pymysql.connect(
            host=os.getenv("DB_HOST"),
            port=int(os.getenv("DB_PORT")),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME"),
            autocommit=True,
        )
        logging.info("Database connection established.")
        return conn
    except pymysql.MySQLError as e:
        logging.error(f"Database connection error: {e}")
        raise

def run_query(query, multi=False):
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        if multi:
            for q in query.split(';'):
                q = q.strip()
                if q:
                    cursor.execute(q)
                    logging.info(f"Executed: {q}")
                    print(f" Executed: {q}")
        else:
            cursor.execute(query)  # send full query with semicolons inside
            logging.info("Query executed successfully.") 
            print(" Query executed successfully.")
    except Exception as e:
        logging.error(f"Query execution failed: {e}")
        print(f" Query execution failed: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
            logging.info("Database connection closed.")
