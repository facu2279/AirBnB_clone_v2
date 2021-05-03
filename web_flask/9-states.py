#!/usr/bin/python3
""" Made by Facundo Diaz for Holberton School 2021 """
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_world():
    """ Returns a specific string """
    return "Hello HBNB!"


@app.route('/hbnb')
def HBNB_world():
    """ Returns a specific string """
    return "HBNB"


@app.route('/c/<text>')
def C_world(text):
    """ Returns all with C """
    return 'C %s' % text.replace('_', ' ')


@app.route('/python/<text>')
@app.route('/python')
def Python_world(text='is cool'):
    """ Returns all with Python """
    return 'Python %s' % text.replace('_', ' ')


@app.route('/number/<int:n>')
def integer_world(n):
    """ Returns all with number """
    return ("{} is a number".format(n))


@app.route('/number_template/<int:n>')
def number_template(n):
    """ Returns number in a html document """
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>')
def oddeven_template(n):
    """ Returns number in a html page """
    return render_template('6-number_odd_or_even.html', number=n)


@app.route('/states_list')
def State_world():
    """ List of states in the database """
    list_states = storage.all(State).values()
    return render_template('7-states_list.html', list_states=list_states)


@app.route('/cities_by_states')
def Cities_World():
    """ List of cities from States in the database """
    list_states = storage.all(State).values()
    return render_template('8-cities_by_states.html', list_states=list_states)


@app.route('/states')
@app.route('/states/<id>')
def StaTeCity_World(id=None):
    """ List of StateCity with filters """
    St_dict = storage.all(State)
    key = "{}.{}".format('State', id)
    return render_template('9-states.html', St_dict=St_dict, id=id, key=key)


@app.teardown_appcontext
def Down_World(exception):
    """ killing the sql session """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
