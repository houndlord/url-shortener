from flask import render_template, flash, redirect, url_for
from flask.wrappers import Request
from werkzeug.wrappers import request
from app import app 
from app import db_conn

@app.route('/', methods =('GET', 'POST'))
def home():
    conn = app.get_db_connection 
    if request.method == 'POST':
        url = request.form['url']

        url.data = conn.execute('INSERT INTO links (url) VALUES (?)',
                            (url,))
        conn.commit()
        conn.close()
    return render_template('home.html')

@app.route('/<id>')
def redirect(id):
    conn = db_conn.get_db_connection
    id = hashids.decode(id)
    if id:
        