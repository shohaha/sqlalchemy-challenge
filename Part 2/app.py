import numpy as np
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify, render_template, request

#################################################
# Database Setup
#################################################

engine = create_engine("sqlite:///../Resources/hawaii.sqlite")

# Reflect an existing database
Base = automap_base()

# Reflect the table
Base.prepare(engine, reflect=True)

# Save reference to tables
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create session
session = Session(engine)

#################################################
# Flask Setup
#################################################

app = Flask(__name__)

#################################################
# Flask Routes
#################################################

# Define Homepage

@app.route("/")
def Home():
    return render_template("index.html")

def calc_temps(start_date, end_date):
    """TMIN, TAVG, and TMAX for a list of dates.
    
    Args:
        start_date (string): A date string in the format %Y-%m-%d
        end_date (string): A date string in the format %Y-%m-%d
        
    Returns:
        TMIN, TAVE, and TMAX
    """
    session = Session(engine)

    return (
        session.query(
            func.min(Measurement.tobs),
            func.avg(Measurement.tobs),
            func.max(Measurement.tobs),
        )
        .filter(Measurement.date >= start_date)
        .filter(Measurement.date <= end_date)
        .all()
    )

# Calculate the date 1 year ago from the last data point in the database
last_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()[0]
last_date = dt.datetime.strptime(last_date, "%Y-%m-%d")
last_year = last_date - dt.timedelta(days=365)

# Define perception query

@app.route("/api/v1.0/precipitation")
def precipitation():
    """Return a dictionary in JSON format where the date is the key and the value is 
    the precipitation data"""

    session = Session(engine)

    # Query all dates and precipitation
    results = session.query(Measurement.date, Measurement.prcp).all()

    session.close()

  # Create a dictionary from the row data and append to a list of all_date_prcp
    all_date_prcp = []
    for date, prcp in results:
        date_prcp_dict = {}
        date_prcp_dict["date"] = date
        date_prcp_dict["prcp"] = prcp
        all_date_prcp.append(date_prcp_dict)

    # Return the valid JSON response object
    return jsonify(all_date_prcp)

# Define stations query

@app.route("/api/v1.0/stations")
def stations():
    """Return a list of stations"""

    session = Session(engine)

    # Query all stations
    results = session.query(Station.station, Station.name).all()

    session.close()

    # Create a dictionary from the row data and append to a list of all_stations
    all_stations = []
    for station, name in results:
        all_stations_dict = {}
        all_stations_dict["station"] = station
        all_stations_dict["name"] = name
        all_stations.append(all_stations_dict)

    return jsonify(all_stations)

# Define dates and temperature (TOBS) query

@app.route("/api/v1.0/tobs")
def tobs():
    """Return a JSON list of temperature observations for the previous year"""

    session = Session(engine)

    # Query all tobs

    results = session.query(Measurement.date,  Measurement.tobs,Measurement.prcp).\
                filter(Measurement.date >= '2016-08-23').\
                filter(Measurement.station=='USC00519281').\
                order_by(Measurement.date).all()

    session.close()

    # Convert the list to Dictionary
    all_tobs = []
    for prcp, date,tobs in results:
        tobs_dict = {}
        tobs_dict["prcp"] = prcp
        tobs_dict["date"] = date
        tobs_dict["tobs"] = tobs
        
        all_tobs.append(tobs_dict)

    return jsonify(all_tobs)

# Define start and end date query

@app.route("/api/v1.0/<start>")
def start(start):
    """Returns the JSON list of the minimum, average and the maximum temperatures for a given start date (YYYY-MM-DD)"""

    temps = calc_temps(start, last_date)

    # Create a list to store the temperature records
    temp_list = []
    date_dict = {"Start Date": start, "End Date": last_date}
    temp_list.append(date_dict)
    temp_list.append(
        {"Observation": "Minimum Temperature", "Temperature(F)": temps[0][0]}
    )
    temp_list.append(
        {"Observation": "Average Temperature", "Temperature(F)": temps[0][1]}
    )
    temp_list.append(
        {"Observation": "Maximum Temperature", "Temperature(F)": temps[0][2]}
    )

    return jsonify(temp_list)


@app.route("/api/v1.0")
def start_end():
    """Returns the JSON list of the minimum, average and the maximum temperatures for a given start date and end date(YYYY-MM-DD)"""
    start = request.args.get("Start Date")
    end = request.args.get("End Date")


    temps = calc_temps(start, end)
    # Create a list to store the temperature records
    temp_list = []
    date_dict = {"Start Date": start, "End Date": end}
    temp_list.append(date_dict)
    temp_list.append(
        {"Observation": "Minimum Temperature", "Temperature(F)": temps[0][0]}
    )
    temp_list.append(
        {"Observation": "Average Temperature", "Temperature(F)": temps[0][1]}
    )
    temp_list.append(
        {"Observation": "Maximum Temperature", "Temperature(F)": temps[0][2]}
    )
    return jsonify(temp_list)

#################################################
# Run application
#################################################
if __name__ == "__main__":
    app.run(debug=True)