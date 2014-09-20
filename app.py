from flask import Flask, render_template, redirect, url_for, flash, request
from jinja2 import Template
from pprint import pprint
import json
app = Flask(__name__)

@app.route('/')
def hello_world():
	return render_template("index.html")

if __name__ == '__main__':
	app.run(debug=True)