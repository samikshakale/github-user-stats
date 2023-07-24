import re
from datetime import datetime
from flask import Flask, request, render_template
from statistics_1 import get_stats

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', error=False)

@app.route('/result', methods=['POST'])
def result():
    username = request.form['username']
    nonforked_str = request.form['nonforked']
    nonforked = (nonforked_str == "true")
    output = get_stats(username, nonforked)
    if output == 0:
        return render_template('home.html', invalid=username, error=True)
    else:
        return render_template('result.html', username=username, nonforked=nonforked, output=output)