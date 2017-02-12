"""Handles the website routing."""

import flask
from flask import render_template

app = flask.Flask(__name__)


@app.route('/')
def home():
    """Renders homepage."""
    return render_template('index.html')


@app.errorhandler(404)
def page_not_found(_):
    """Return a 404 error."""
    return '', 404
