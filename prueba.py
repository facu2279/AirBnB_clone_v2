#!/usr/bin/python3
""" Write a script that starts a Flask web application """
from flask import Flask, render_template
from models import storage
from models.state import State


list_states = storage.all(State).values()
print(list_states)
