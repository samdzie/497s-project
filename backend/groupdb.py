import flask
from flask import request, jsonify
import sqlite3
from sqlite3 import Error

app = flask.Flask(__name__)
app.config["DEBUG"] = True

#Need to figure out how to hook up to Postman
#Currently needs a preexisting events.db on local drive

@app.route('/events', methods =['GET'])
def home():
    #Welcome screen
    return '''<h1>Flask Group events database api</h1>
    <p>A WIP API for group events</p>'''


@app.route('/events/all', methods=['GET'])
def api_all():
    #Connects to a preexisting events.db and returns all events made
    Database = 'events.db'
    try:
            conn = sqlite3.connect(Database)
            cursor = conn.cursor()
            all_events = cursor.execute('SELECT * FROM EventsTable;').fetchall()

    except Error as e:
        print(e)

    return jsonify(all_events)


@app.route('/events/createtable', methods=['POST'])
def creat_table():
    #Creates a table
    Database = 'events.db'
    conn = sqlite3.connect(Database)
    conn.execute(''' 
    CREATE TABLE EventsTable (
        ID int,
        Subject text,
        Description text
    );
    ''')
    conn.close()


# @app.route('/events/newevent', methods=['POST'])
# def creat_event():
#     #Creates an event
#     #Make an html file for the user to fill out for events??
#     Database = 'events.db'
#     conn = sqlite3.connect(Database)
#     conn.execute('INSERT ')


#Update event
#Delete event


@app.errorhandler(404)
def page_not_found(e):
    #Error message if resource isn't found
    return '''
    <h1>Error 404 Page not found</h1>
    <p>Page resources could not be found. </p>
    ''', 404

app.run()