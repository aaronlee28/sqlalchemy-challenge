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
        f'/api/v1.0/tobs<br/>'
        f'/api/v1.0/start<br/>'
        f'/api/v1.0/start/end<br/>'
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


@app.route("/api/v1.0/<start>")
def start_date(start):
    # Create our session (link) from Python to the DB
    session = Session(engine)
    # date_tobs = session.query(Measurement.date, Measurement.tobs).all()

    # Queries the min, max, and average temperature 
    min_start = session.query(func.min(Measurement.tobs)).filter(Measurement.date >= start).all()
    avg_start = session.query(func.avg(Measurement.tobs)).filter(Measurement.date >= start).all()
    max_start = session.query(func.max(Measurement.tobs)).filter(Measurement.date >= start).all()
    # queries = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start).all()

    # Create a dictionary
    output_start = [{"tmin": min_start, 'tavg': avg_start, 'tmax': avg_start}]

    # Close session
    session.close ()

    return jsonify(output_start)

@app.route("/api/v1.0/<start>/<end>")
def start_end_date(start,end):
    # Create our session (link) from Python to the DB
    session = Session(engine)
    # date_tobs_1= session.query(Measurement.date, Measurement.tobs).all()

    # Queries the min, max, and average temperature 
    min_start_end = session.query(func.min(Measurement.tobs)).filter(Measurement.date.between(start,end)).all()
    avg_start_end = session.query(func.avg(Measurement.tobs)).filter(Measurement.date.between(start,end)).all()
    max_start_end= session.query(func.max(Measurement.tobs)).filter(Measurement.date.between(start,end)).all()
    # queries = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start).all()

    # Create a dictionary
    output_start_end = [{"tmin": min_start_end, 'tavg': avg_start_end, 'tmax': max_start_end}]

    # Close session
    session.close ()

    return jsonify(output_start_end)


if __name__ == "__main__":
    app.run(debug=True)