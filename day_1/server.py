import datetime as dt
from flask import Flask

app = Flask(__name__)
now = dt.datetime.now()


@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/status")
def status():
    return {
        'Status': True,
        'Time': now.strftime("%d-%m-%Y %H:%M")
    }


app.run()
