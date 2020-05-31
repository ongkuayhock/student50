## Use flask for web
##
## Use following command to run flask web server
## 1. env FLASK_APP=hello.py flask run
## 2. export FLASK_APP=xxx to set environment variable and then run fask run
##
from flask import Flask, render_template , request
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("indexPost.html")

@app.route("/hello", methods = ["GET", "POST"])
def hello():
    if request.method == "GET":
        return("Please subnit the form isntead")
    else:
        name = request.form.get("name")
        return render_template("hello.html" , name = name)

@app.route("/Keith")
def david():
    return(f"<h1 style='color:blue;'> Hello Keith - for you. Amazing!!!</h1>")
