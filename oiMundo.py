#!/usr/bin/python3

from flask import Flask

app = Flask(__name__)

@app.route("/")
def oimundo():
    return 'Oi Mundo!'

if (__name__ == "__main__"):
    app.run()
