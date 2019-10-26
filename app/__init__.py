from flask import Flask, render_template

app = Flask(__name__)

from app import sql_connection

@app.route("/demo")
def hello():
    return render_template('first.html')
