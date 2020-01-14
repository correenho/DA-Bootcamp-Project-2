import os

import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template
# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


#################################################
# Database Setup
#######################
##########################

# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/Zillow_database.sqlite"
# db = SQLAlchemy(app)

# # reflect an existing database into a new model
# Base = automap_base()
# # reflect the tables
# Base.prepare(db.engine, reflect=True)

# # Save references to each table
# buy_list = Base.classes.buy_list
# rent_list = Base.classes.rent_list


@app.route("/")
def index_map():
    """Return the homepage."""
    return render_template("index_map.html")


# @app.route("/buy_list")
# def names():
#     """Return a list of sample names."""

#     # Use Pandas to perform the sql query
#     stmt = db.session.query(buy_list).statement
#     df = pd.read_sql_query(stmt, db.session.bind)

#     # Return a list of the column names
#     return jsonify(list(df.columns))


# @app.route("/buy_metadata/<address>")
# def buy_metadata(address):
#     """Return the MetaData for a given address."""
#     sel = [
#         buy_list.address,
#         buy_list.price,
#         buy_list.details,
#         buy_list.zipcode,
#         buy_list.zpid,
#         buy_list.link,
#     ]

#     result = db.session.query(*sel).filter(buy_list.address == address).all()

#     # Create a dictionary entry for each row of metadata information
#     sample_metadata = {}
#         sample_metadata["address"] = result[0]
#         sample_metadata["ETHNICITY"] = result[1]
#         sample_metadata["GENDER"] = result[2]
#         sample_metadata["AGE"] = result[3]
#         sample_metadata["LOCATION"] = result[4]
#         sample_metadata["BBTYPE"] = result[5]
#         sample_metadata["WFREQ"] = result[6]

#     print(sample_metadata)
#     return jsonify(sample_metadata)


# @app.route("/samples/<sample>")
# def samples(sample):
#     """Return `otu_ids`, `otu_labels`,and `sample_values`."""
#     stmt = db.session.query(Samples).statement
#     df = pd.read_sql_query(stmt, db.session.bind)

#     # Filter the data based on the sample number and
#     # only keep rows with values above 1
#     sample_data = df.loc[df[sample] > 1, ["otu_id", "otu_label", sample]]

#     # Sort by sample
#     sample_data.sort_values(by=sample, ascending=False, inplace=True)

#     # Format the data to send as json
#     data = {
#         "otu_ids": sample_data.otu_id.values.tolist(),
#         "sample_values": sample_data[sample].values.tolist(),
#         "otu_labels": sample_data.otu_label.tolist(),
#     }
#     return jsonify(data)



# @app.route("/pricetrends")
# def pricetrends():
    
#     return render_template("index.html")




# @app.route("/school")
# def school():

#     return render_template("index_school.html")
   


if __name__ == "__main__":
    app.run(debug=True)