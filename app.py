from flask import Flask, render_template, redirect, url_for, flash, request
from flask.ext import restful
from flask.ext.pymongo import PyMongo
from flask import make_response
from bson.json_util import dumps
from jinja2 import Template
from pprint import pprint
import json

MONGO_URL = os.environ.get('MONGO_URL')
if not MONGO_URL:
	MONGO_URL = "mongodb://localhost:27017/rest"

app = Flask(__name__)

app.config['MONGO_URI'] = MONGO_URL
mongo = PyMongo(app)

def output_json(obj, code, headers=None):
	resp = make_response(dumps(obj), code)
	resp.headers.extend(headers or {})
	return resp

DEFAULT_REPRESENTATIONS = {'application/json': output_json}
api = restful.Api(app)
api.representations = DEFAULT_REPRESENTATIONS

import flask_rest_service.resources

@app.route('/')
def index():
	def load_json(file):
		data = open(file)
		cards = json.load(data)

	cards =	load_json("static/cards.json")

	print cards

	return render_template("index.html", data = cards)

if __name__ == '__main__':
	app.run(debug=True)