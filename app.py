from flask import Flask, render_template, redirect, url_for, flash, request
from flask import make_response
from jinja2 import Template
import json

app = Flask(__name__)

@app.route('/')
def match():
	return render_template("match.html")

@app.route('/gallery')
def map():
	return render_template("gallery.html")

@app.route('/presentation')
def about():
	return render_template("hackthehearst.html")

if __name__ == '__main__':
	app.run(debug=True)