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


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ display a HTML page """
    info = storage.all(State).values()
    return render_template('7-states_list.html', states=info)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """ok
    """
    info = {
        'states': storage.all(State).values(),
        'cities': storage.all(City).values()
    }
    return render_template('8-cities_by_states.html', **info)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
