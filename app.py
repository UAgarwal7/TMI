from flask import Flask
app = Flask(__name__)

@app.route("/")
def testing():
    x = 4
    return x
def index():
    return testing
