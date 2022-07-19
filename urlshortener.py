from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'

from shortener import routes

#app.run(host = '127.0.0.2:5001', debug=True)
if __name__ == "__main__":
    app.run(host = "127.0.0.2", debug=True)