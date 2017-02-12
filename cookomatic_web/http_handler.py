"""Handles the HTTP routing."""

import flask
from flask import render_template

app = flask.Flask(__name__)
app.config['DEBUG'] = True

SUCCESS = ('', 200)


@app.route('/ping')
def ping():
    """Sample web handler to see if the server is alive."""
    return 'pong'


@app.route('/')
def home_page():
    """Sample web handler to see if the server is alive."""
    return render_template('index.html')


@app.errorhandler(404)
def page_not_found(error):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL. Error msg: %s' % error, 404
