#!/usr/bin/python3
''' Made by Facundo Diaz for Holberton School 2021'''
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    '''This part show on html pages'''
    s_list = storage.all(State).values()
    a_list = storage.all(Amenity).values()
    return render_template("10-hbnb_filters.html", s_list=s_list, a_list=a_list)


@app.teardown_appcontext
def teardown_db(exception):
    '''This function killing the sql session'''
    storage.close()

if __name__ == '__main__':
    ''' xdxd '''
    app.run(host='0.0.0.0', port=5000)
