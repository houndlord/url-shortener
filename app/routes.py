from flask import render_template, flash, redirect, url_for
from flask.wrappers import Request
from werkzeug.wrappers import request
import psycopg2
from db_conn import get_db_connection
from app import app 

@app.route('/h')
def debil():
    return "ebil"

@app.route('/index', methods =('GET', 'POST'))
def home():
    print("fdsf")
    conn = get_db_connection()
    if request.method == 'POST':
        url = request.form['url']

        url.data = conn.execute('INSERT INTO links (url) VALUES (?)',
                            (url,))
        conn.commit()
        conn.close()
    return render_template('home.html')

@app.route('/<id>')
def redirect(id):
    conn = get_db_connection()
    conn.execute('SELECT * FROM Links where (%s) == id;', (id))
    res = conn.fetchone()
    return redirect(res)