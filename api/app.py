"""A Flask API for the web app."""

import random
import string
from datetime import datetime, timedelta
from flask import Flask, jsonify, make_response


app = Flask(__name__)


def random_event():
    """Generate a random event object.

    The event begins at a random time in 2020 and lasts for a random
    multiple of 15 minutes in the range of 15 minutes to 4 hours.
    """
    title = ''.join(random.choices(string.ascii_lowercase, k=10))
    start_ts = datetime(year=2020, month=1, day=1).timestamp()
    end_ts = datetime(year=2020, month=12, day=31).timestamp()
    start_ts = start_ts + random.random() * (end_ts - start_ts)
    start = datetime.fromtimestamp(start_ts)
    end = start + timedelta(minutes=(15 * random.randint(1, 16)))
    return {
        'title' : title,
        'start' : start,
        'end' : end
    }


@app.route('/api')
def hello_world():
    """A welcome message to verify a connection to the API."""
    return 'Welcome to the API!'


@app.route('/api/events')
def get_events():
    """Return a list of all stored events in ascending order of start
    time."""
    events = {
        'events' : [random_event() for _ in range(10)]
    }
    events['events'] = sorted(events['events'], key=lambda x: x['start'])
    response = make_response(events)
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response
