import psycopg2

def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='flask_db',
                            user='DB_USERNAME',
                            password='DB_PASSWORD')
    return conn
