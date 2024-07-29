"""Contains a Flask application"""


from flask import Flask

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)