## Use flask for web
##
## Use following command to run flask web server
## 1. env FLASK_APP=hello.py flask run
## 2. export FLASK_APP=xxx to set environment variable and then run fask run
##
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    tmpline2 = "Passing a Flag on"
    return render_template("test.html", headline2 = tmpline2 )

@app.route("/Keith")
def david():
    return(f"<h1 style='color:blue;'> Hello Keith - for you. Amazing!!!</h1>")

@app.route("/<string:namef>")
def Hello(namef):
    namef = namef + ".html"
    return render_template( namef )


    