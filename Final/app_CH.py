from flask import Flask
from flask import render_template
from pymongo import MongoClient
import json
from bson import json_util
from bson.json_util import dumps
import os
import sqlite3
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy


from flask import Flask, jsonify, render_template
# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#################################################
# Database Setup
#################################################

MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
DBS_NAME = 'project2'


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
	return render_template("index_ch.html")

@app.route("/map")
def index_map():
    """Return the homepage."""
    return render_template("index_map.html")


@app.route("/school")
def school():
    return render_template("school.html")
    
@app.route("/crime")
def crime():
    return render_template("crime.html")    

@app.route("/project2/lbdemographics")
def project2_lbdemographics():

    COLLECTION_NAME = 'lbdemographics'
    FIELDS =  FIELDS = {'Name':True, 'African_American':True, 
                    'American_Indian_or_Alaska_Native':True, 'Asian': True, 
                    'Filipino':True, 'Hispanic_or_Latino': True,
                    'Pacific_Islander': True,'White':True, 
                    'Two_or_more':True, 'Not_Reported':True ,'_id':False}
                    
    connection = MongoClient(MONGODB_HOST, MONGODB_PORT)
    collection = connection[DBS_NAME][COLLECTION_NAME]
    lbdemographics = collection.find(projection=FIELDS)
    jsonDemo = []
    for demo in lbdemographics:
        jsonDemo.append(demo)
    jsonDemo= json.dumps(jsonDemo, default=json_util.default)
    connection.close()
    return jsonDemo
    
@app.route("/project2/absent")
def project2_absent():

    COLLECTION_NAME = 'absent'
    FIELDS =  FIELDS = {'Name':True, 'Eligible_Enrollment':True, 
                    'Chronic_Absenteeism_Count':True, '_id':False}
                    
    connection = MongoClient(MONGODB_HOST, MONGODB_PORT)
    collection = connection[DBS_NAME][COLLECTION_NAME]
    absentData = collection.find(projection=FIELDS)
    jsonAbsent = []
    for student in absentData:
        jsonAbsent.append(student)
    jsonAbsent= json.dumps(jsonAbsent, default=json_util.default)
    connection.close()
    return jsonAbsent
    
@app.route("/project2/english")
def project2_english():

    COLLECTION_NAME = 'english'
    FIELDS =  FIELDS = {'Name':True, 'English_Only':True, 
                    'Initial_Fluent_English_Proficient':True,
                    'English_Learner': True, 'Reclassified_Fluent_English_Proficient':True,
                    'To_Be_Determined':True, 'Total':True,
                    '_id':False}
                    
    connection = MongoClient(MONGODB_HOST, MONGODB_PORT)
    collection = connection[DBS_NAME][COLLECTION_NAME]
    englishData = collection.find(projection=FIELDS)
    jsonEnglish = []
    for student in englishData:
        jsonEnglish.append(student)
    jsonEnglish= json.dumps(jsonEnglish, default=json_util.default)
    connection.close()
    return jsonEnglish
    
@app.route("/project2/staff")
def project2_staff():

    COLLECTION_NAME = 'staff'
    FIELDS =  FIELDS = {'Name':True, 'Doctorate':True, 
                    'Juris_Doctor':True,
                    'Masters_Degree_30': True, 'Masters_Degree':True,
                    'Baccalaureate_Degree_30':True, 'Baccalaureate_Degree':True,
                    'None_Reported':True, 'Total': True,
                    '_id':False}
                    
    connection = MongoClient(MONGODB_HOST, MONGODB_PORT)
    collection = connection[DBS_NAME][COLLECTION_NAME]
    staffData = collection.find(projection=FIELDS)
    jsonStaff = []
    for staff in staffData:
        jsonStaff.append(staff)
    jsonStaff= json.dumps(jsonStaff, default=json_util.default)
    connection.close()
    return jsonStaff
    
@app.route("/project2/suspension")
def project2_suspension():

    COLLECTION_NAME = 'suspension'
    FIELDS =  FIELDS = {'Name':True, 'Cumulative_Enrollment':True, 
                    'Total_Suspensions':True,
                    'Unduplicated_Suspensions': True,
                    '_id':False}
                    
    connection = MongoClient(MONGODB_HOST, MONGODB_PORT)
    collection = connection[DBS_NAME][COLLECTION_NAME]
    suspensionData = collection.find(projection=FIELDS)
    jsonSuspension = []
    for student in suspensionData:
        jsonSuspension.append(student)
    jsonSuspension= json.dumps(jsonSuspension, default=json_util.default)
    connection.close()
    return jsonSuspension
@app.route("/indexjas")
def indexjas():
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



if __name__ == "__main__":
    app.run(debug=True)
