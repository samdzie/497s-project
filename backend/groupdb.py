"""

A group event database. Creating, reading, updating, and deleteing JSON objects in SQLAlchemy.


"""


from flask import Flask, abort, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# Do not track modifications to save overhead
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Events(db.Model):
    """A SQLAlchemy model representing a table of Events """
    # id is an integer and serves as a primary key (i.e., unique identifier)
    id = db.Column(db.Integer, primary_key = True)
    # Title and description are strings that cannot be null 
    title = db.Column(db.String(80), nullable = False)
    description = db.Column(db.String(80), nullable = False)
    # Maybe additional information like including participants? 
    # Participants could be simple strings like title or something like a user id

db.create_all()

class EventsSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Events # Generate the schema from the above Events model
        load_instance = True

    # Automatically fill these fields
    id = auto_field()
    title = auto_field()
    description = auto_field()

@app.route('/')
def hello_world():
    """Returns a string for testing """
    return 'Hello World!'

@app.route('/events', methods = ['POST'])
def create_events():
    """Creates an Events table from a POSTed JSON object. """
    # If the request has no JSON, respond HTTP 400
    json = request.json 
    if json is None:
        abort(400)
    # If the JSON exists but has no title or artist, respond HTTP 400
    title = json.get('title')
    description = json.get('description')

    if title is None or description is None:
        abort(400)
    
    # Create the Events object
    events = Events(title = title, description = description)
    # Add it to the database
    db.session.add(events)
    db.session.commit()
    # Serialize the album as a JSON object and return it
    schema - EventsSchema()
    return jsonify(schema.dump(events))

@app.route('/events/<events_id>')
def get_events(events_id):
    """Returns the events with the given id as a JSON object. """
    # Filter events matching events_id and select the first one found
    events = Events.query.filter_by(id=events_id).first()
    # If no events matches album_id, respond HTTP 404
    if events is None:
        abort(404)
    # Serialize the album as a JSON object and return it
    schema = EventsSchema()
    return jsonify(schema.dump(events))


@app.route('/events/<events_id>', methods=['PUT'])
def update_events():
    """ Update the events with the given ID. """
    #If the request has no JSON, respond HTTP 400
    json = request.json
    if json is None:
        abort(400)
    # Filter events matching events_id and select the first one found
    events = Events.query.filter_by(id = events_id).first()
    # If no events matches events_id, respond HTTP 404
    if album is None:
        abort(404)
    # Update the title and/or description, if present in JSON
    if 'title' in json: 
        events.title = json.get('title')
    if 'description' in json:
        events.description = json.get('description')
    # Add it to the database
    db.session.add(events)
    db.session.commit()
    # Serialize the events as a JSON object and return it
    schema = EventsSchema()
    return jsonify(schema.dump(events))


@app.route('/events/<events_id>', methods = ['DELETE'])
def delete_event(events_id):
    """ Delete the event with the given ID. """
    # Filter events matching events_id and select the first one found
    events = Events.query.filter_by(id = events_id).first()
    # If no events matches events_id, respond HTTP 404
    if events is None:
        abort(404)
    # Delete it from database
    db.session.delete(events)
    db.session.commit()
    # Serialize the events as a JSON object and return it
    schema = EventsSchema()
    return jsonify(schema.dump(events))
