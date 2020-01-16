import os
import sqlite3

import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#################################################
# Database Setup
#################################################
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///LB_database.sqlite"
db = SQLAlchemy(app)
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(db.engine, reflect=True)
# Save references to each table
LB_hvi = Base.classes.LB_hvi
LB_Rent_Sqft = Base.classes.LB_Rent_Sqft
LB_Rent_Unit = Base.classes.LB_Rent_Unit

@app.route("/")
def index():
    """Return the homepage."""
    return render_template("indexjas.html")

@app.route("/page2")
def page2():
    """Return the homepage."""
    return render_template("rent_sqft.html")

@app.route("/page3")
def page3():
    """Return the homepage."""
    return render_template("rent_unit.html")

@app.route("/lineChart/<chartType>")
def lineChart(chartType):

	conn = sqlite3.connect('LB_database.sqlite')
	c = conn.cursor() #cursor allows you to run SQL commands using execute method

	output = []
	sql_data = []
	col = ['January', 'February', 'March','April', 'May', 'June', 
			'July', 'August', 'September','October', 'November']

	if chartType == "homeValue":
		#print('homeValue')
		try:
			c.execute("""SELECT January, February, March,
			April, May, June, July, August, September,
			October, November FROM LB_hvi ORDER BY id""")

			sql_data = c.fetchall()

		except Exception as e:
			print(e)

	elif chartType == 'RentSqft':
		try:
			c.execute("""SELECT January, February, March,
			April, May, June, July, August, September,
			October, November FROM LB_Rent_Sqft ORDER BY id""")

			sql_data = c.fetchall()

		except Exception as e:
			print(e)

	elif chartType == 'RentUnit':
		try:
			c.execute("""SELECT January, February, March,
			April, May, June, July, August, September,
			October, November FROM LB_Rent_Unit ORDER BY id""")

			sql_data = c.fetchall()

		except Exception as e:
			print(e)

	# print(str(sql_data))
	bedroom = ['1 Bedroom', '2 Bedroom', '3 Bedroom', '4 Bedroom', '5 Bedroom' ]
	for i, row in enumerate (sql_data):
		trace = {
		'x': col,
		'y': row,
		'mode': 'lines+markers',
		'name': bedroom[i],
		'line': {'shape': 'linear'}
		}
		output.append(trace)

	conn.close()
	return jsonify(output)


if __name__ == '__main__':
	app.run(debug=True)