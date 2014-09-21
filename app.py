from flask import Flask, render_template, redirect, url_for, flash, request
from jinja2 import Template
from pprint import pprint
import json
app = Flask(__name__)

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