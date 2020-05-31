## Use flask for web
##
## Use following command to run flask web server
## 1. env FLASK_APP=hello.py flask run
## 2. export FLASK_APP=xxx to set environment variable and then run fask run
##
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return("<h1 style='color:red;'> Hello world - Good progress. Amazing!!!</h1>")
##    return "<h1 style='color: red;'>I'm a red H1 heading!</h1>"

@app.route("/<string:name>")
def Hello(name):
    return(f"<h1 style='color:blue;'> Hello {name} - for you. Amazing!!!</h1>")


    