from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello! This is the main page."

@app.route("/testing")
def testing():
    return "Testing this out"
