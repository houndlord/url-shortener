import os 
import psycopg2

def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='links',
                            user=os.environ['DB_USERNAME'],
                            password=os.environ['DB_PASSWORD'])
    return conn
