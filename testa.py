# -*- coding:utf-8 -*-

from flask import Flask, render_template

import data

data.init()

app = Flask(__name__)
@app.route("/")
def home():
    return render_template('index.html')


@app.route("/list")
def list():
    return render_template('list.html', projects = data.retrieve_projects()[1])

@app.route("/techniques")
def techniques():
    return render_template('techniques.html', techniques = data.retrieve_techniques()[1])


@app.route("/search/<id>")
def search(id):
    return render_template('search.html', search_results = data.retrieve_projects(search=str(id), search_fields=[None])[1])


if __name__ == "__main__":
    app.run(debug = True)
