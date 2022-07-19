import os
import psycopg2

conn = psycopg2.connect(
        host="localhost",
        #database="flask_db",
        user=os.environ['DB_USERNAME'],
        password=os.environ['DB_PASSWORD'])
conn.set_session(autocommit = True)

cur = conn.cursor()

#cur.execute("CREATE DATABASE Links")

cur.execute('DROP TABLE IF EXISTS links;')
cur.execute('CREATE TABLE links ('
    'id INTEGER PRIMARY KEY,'
    'url TEXT NOT NULL,'
    'shortlink TEXT NOT NULL);'
)
conn.commit()

cur.close()
conn.close()