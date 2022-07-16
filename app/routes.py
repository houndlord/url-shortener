from flask import render_template, flash, redirect, url_for
from flask.wrappers import Request
from werkzeug.wrappers import request
import psycopg2
from .db_conn import get_db_connection
from .forms import URLForm
from app import app 


@app.route('/h')
def debil():
    return "ebil"

@app.route('/index')
def some():
    form = URLForm()
    return render_template('index.html', form = form)

@app.route('/index', methods =('GET', 'POST'))
def home():
    print("fdsf")
    form = URLForm()
    if form.validate_on_submit():
        url = URLForm.url
        conn = get_db_connection()
        conn.execute('INSERT INTO links (%s) VALUES (?)',
                            (url))
        conn.commit()
        conn.close()
        return render_template('home.html', form = form)

@app.route('/<id>')
def redirect(id):
    conn = get_db_connection()
    conn.execute('SELECT * FROM Links where (%s) == id;', (id))
    res = conn.fetchone()
    return redirect(res)