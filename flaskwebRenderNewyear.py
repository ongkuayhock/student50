## Use flask for web
##
## Use following command to run flask web server
## 1. env FLASK_APP=hello.py flask run
## 2. export FLASK_APP=xxx to set environment variable and then run fask run
##
from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    now = datetime.now()
    newyear = (now.month == 1) and (now.day == 1)
    return render_template("index.html" , newyear = newyear )

@app.route("/Name")
def namel():
    names = ["Charles" , "Charlene" , "Charlotte"]
    return render_template("indexlist1.html" , names = names)

@app.route("/Keith")
def david():
    return(f"<h1 style='color:blue;'> Hello Keith - for you. Amazing!!!</h1>")

@app.route("/<string:namef>")
def Hello(namef):
    namef = namef + ".html"
    return render_template( namef )


    