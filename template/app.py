"""A template Flask app for creating new services.

Please include a descriptive docstring like this at the beginning of
your code. It should give a one-line summary of its purpose and more
details below if it would help readers understand your code.

Be sure to use comments and docstrings to make your code readable!
It'll help both you and other developers.
"""
from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello_world():
    """A simple hello world for testing."""
    return 'hello world!'
