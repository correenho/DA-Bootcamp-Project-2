from flask import Flask
from flask import render_template
from pymongo import MongoClient
import json
from bson import json_util
from bson.json_util import dumps

app = Flask(__name__)

MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
DBS_NAME = 'project2'


@app.route("/")
def school():
    return render_template("school.html")

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

if __name__ == "__main__":
    app.run(debug=True)
