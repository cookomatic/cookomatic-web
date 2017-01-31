"""Handles the HTTP routing."""

import flask
from flask import render_template

APP = flask.Flask(__name__)
APP.config['DEBUG'] = True

SUCCESS = ('', 200)


@APP.route('/ping')
def ping():
    """Sample web handler to see if the server is alive."""
    return 'pong'


@APP.route('/')
def home_page():
    """Sample web handler to see if the server is alive."""
    return render_template('index.html')


@APP.errorhandler(404)
def page_not_found(error):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL. Error msg: %s' % error, 404
