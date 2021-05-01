#!/usr/bin/python3
""" Write a script that starts a Flask web application """
from flask import Flask, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_world():
    """ Returns Hello HBNB """
    return "Hello HBNB!"


@app.route('/hbnb')
def HBNB_world():
    """ Returns HBNB """
    return "HBNB"


@app.route('/c/<text>')
def C_world(text):
    """ Returns something with C """
    return 'C %s' % text.replace('_', ' ')


@app.route('/python/<text>')
@app.route('/python')
def Python_world(text='is cool'):
    """ Returns something with Python """
    return 'Python %s' % text.replace('_', ' ')


@app.route('/number/<int:n>')
def integer_world(n):
    """ Returns something with number """
    return ("{} is a number".format(n))


@app.route('/number_template/<int:n>')
def number_template(n):
    """ Returns number in template """
    return render_template('5-number.html', number=n)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
