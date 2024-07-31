#!/usr/bin/python3

"""Contains a Flask application"""


from flask import Flask, abort

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Creates the route to Home"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Creates a route to hbnb"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def show_c(text):
    """Create the c route with parameter"""
    new = text.replace('_', ' ')
    return f'C {new}'


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def show_python(text='cool'):
    """Creates a route for python"""
    new = text.replace('_', ' ')
    return f'Python {new}'


@app.route('/number/<n>', strict_slashes=False)
def number(n):
    """Create route to number"""
    try:
        num = int(n)
        return f'{num} is a number'
    except(Exception):
        abort(404)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
