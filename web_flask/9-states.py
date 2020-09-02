#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City


app = Flask(__name__)


@app.teardown_appcontext
def teardown(self):
    """reload close files storage"""
    storage.close()


@app.route('/states', strict_slashes=False)
@app.route('/states_list', strict_slashes=False)
def states_list():
    """ display a HTML page """
    info = storage.all(State).values()
    return render_template('7-states_list.html', states=info)


@app.route('/states/<id>', strict_slashes=False)
def statesId(id):
    """[summary]

    Args:
        id ([type]): [description]
    """
    states = storage.all(State)
    key = 'State.{}'.format(id)
    if key in states:
        state = states[key]
    else:
        state = None
    return render_template('9-states.html', state=state)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
