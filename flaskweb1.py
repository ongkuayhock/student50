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
    return("Hello world - Good progress. Amazing!!!")

@app.route("/David")
def David():
    return("Hello David - for you. Amazing!!!")


    