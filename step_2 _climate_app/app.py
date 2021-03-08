from matplotlib import style
import matplotlib.pyplot as plt
from flask import Flask, jsonify

import numpy as np
import pandas as pd
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect, desc

# Database Setup
engine = create_engine("sqlite:///../step_1_climate_analysis_and_exploration/resources/hawaii.sqlite")

# Reflect an existing database into a new model 
Base = automap_base() 

# Reflect tables 
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station


# Flask Setup
app = Flask(__name__)

# Flask Routes 
@app.route("/")
def welcome():
    return (
        f'Welcome to the Climate App API<br/>'
        f'/api/v1.0/precipitation<br/>'
        f'/api/v1.0/stations<br/>'
        f'/api/v1.0/tobs'
        f'/api/v1.0/<start><br/>'
        f'/api/v1.0/<start>/<end><br/>'
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    # Query all precipitation
    precipitation = session.query(Measurement.date, Measurement.prcp).all()
    session.close ()

    # Convert list of tuples into normal list 
    all_prcp = list(np.ravel(precipitation))

    return jsonify(all_prcp)


@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    # Query all precipitation
    station = session.query(Measurement.station).all()
    session.close ()

    # Convert list of tuples into normal list 
    all_station = list(np.ravel(station))

    return jsonify(all_station)

@app.route("/api/v1.0/tobs")
def tobs():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    # Query all precipitation
    tobs = session.query(Measurement.date, Measurement.tobs).filter(Measurement.date.between('2016-08-23', '2017-08-23'),
        (Measurement.station == 'USC00519281')).all()
    session.close ()

    # Convert list of tuples into normal list 
    all_tobs = list(np.ravel(tobs))

    return jsonify(tobs)





if __name__ == "__main__":
    app.run(debug=True)
