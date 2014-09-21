from flask import Flask, render_template, redirect, url_for, flash, request
from flask.ext import restful
from flask.ext.pymongo import PyMongo
from flask import make_response
from bson.json_util import dumps
from jinja2 import Template
from pprint import pprint
import json
from flask_rest_service import app

app.run(debug=True)

# @app.route('/')
# def index():
# 	def load_json(file):
# 		data = open(file)
# 		cards = json.load(data)

# 	cards =	load_json("static/cards.json")

# 	print cards

# 	return render_template("index.html", data = cards)

# if __name__ == '__main__':
# 	app.run(debug=True)