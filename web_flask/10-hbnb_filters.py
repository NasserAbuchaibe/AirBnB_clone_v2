#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from os import getenv


app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """[summary]
    """
    sta = storage.all(State).values()
    ame = storage.all(Amenity).values()
    return render_template('10-hbnb_filters.html', states=sta, amenities=ame)


@app.teardown_appcontext
def teardown(self):
    """reload close files storage"""
    storage.close()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
