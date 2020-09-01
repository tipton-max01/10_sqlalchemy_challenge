import numpy as np
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask
from flask import jsonify

# Database Setup
engine = create_engine("sqlite:///hawaii.sqlite")
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)
# We can view all of the classes that automap found
Base.classes.keys()
#Measurement = Base.classes.measurement
#Station = Base.classes.station

# Flask Setup
#Create an app, being sure to pass __name__
app = Flask(__name__)

#Define what to do when a user hits the index route
@app.route("/")
def home():
    print("Server received request for 'Home' page...")
    return (f"Welcome to my climate API for Hawaii. Surf's Up!"
            f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<br/>"
            f"Available Routes:<br/>"




if __name__ == "__main__":
    app.run(debug=True)
