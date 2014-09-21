from flask import Flask, render_template, redirect, url_for, flash, request
from flask.ext import restful
from flask.ext.pymongo import PyMongo
from flask import make_response
from bson.json_util import dumps
from jinja2 import Template
from pprint import pprint
import json
from flask import jsonify
# from flask_rest_service import app

app = Flask(__name__)

@app.route('/')
def match():
	return render_template("match.html")

@app.route('/gallery')
def map():
	return render_template("gallery.html")

if __name__ == '__main__':
	app.run(debug=True)