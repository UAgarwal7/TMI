from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
#    return render_template("templates/home.html")

@app.route("/testing")
def testing():
    return "Testing this out."
