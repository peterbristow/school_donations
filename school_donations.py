from flask import Flask
from flask import render_template
from pymongo import MongoClient
import json

app = Flask(__name__)

# MONGODB_HOST = 'localhost'
# MONGODB_PORT = 27017
# DBS_NAME = 'donorsUSA'

MONGODB_HOST = 'ds013941.mlab.com' # This time we won't be using the digits after the colon - eg. ds047305.mlab.com
MONGODB_PORT = 13941 # This is for the port. This where the digits after the colon go. These will be integers - eg. 47305
DBS_NAME = 'heroku_0c2hzqn6' # Your database name - eg. heroku_1wgm307k
MONGO_URI = 'mongodb://root:hp271008M@ds013941.mlab.com:13941/heroku_0c2hzqn6'

COLLECTION_NAME = 'projects'
FIELDS = {'funding_status': True, 'school_state': True, 'resource_type': True, 'poverty_level': True,
          'primary_focus_area': True, 'date_posted': True, 'total_donations': True, '_id': False}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/donorsUS/projects")
def donor_projects():
    # connection = MongoClient(MONGODB_HOST, MONGODB_PORT)
    # collection = connection[DBS_NAME][COLLECTION_NAME]
    # projects = collection.find(projection=FIELDS, limit=55000)
    connection = MongoClient(MONGO_URI)
    collection = connection[DBS_NAME][COLLECTION_NAME]
    projects = collection.find(projection=FIELDS, limit=20000)
    json_projects = []
    for project in projects:
        json_projects.append(project)
    json_projects = json.dumps(json_projects)
    connection.close()
    return json_projects


if __name__ == "__main__":
    app.run(debug=True)
