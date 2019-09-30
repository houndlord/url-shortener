from flask import Flask, render_template, redirect, request
from config import Config
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

#from app import routes, models

@app.route("/")
def home():
    return render_template('home.html')

@app.route


if __name__ == "__main__":
    app.run(debug=True)