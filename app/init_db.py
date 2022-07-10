import os
import psycopg2

conn = psycopg2.connect(
        host="localhost",
        database="flask_db",
        user=os.environ['DB_USER'],
        password=os.environ['DB_PASSWORD'])
conn.set_session(autocommit = True)

cur = conn.cursor()

cur.execute("CREATE DATABASE Links")

conn.execute('DROP TABLE IF EXISTS links;')
conn.execute('CREATE TABLE links ('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'url TEXT NOT NULL'
    'shortlink TEXT NOT NULL);'
)
conn.commit()

cur.close()
conn.close()