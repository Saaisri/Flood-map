from flask import Flask, render_template,request
import pymongo
from pymongo import MongoClient
import os
import json
from bson import json_util

app = Flask('test', template_folder= 'templates')


cluster = pymongo.MongoClient('mongodb+srv://flap:flap098@cluster0.efrpc.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db = cluster["result"]
pollcol = db["poll"]

#index
@app.route('/')
def index():
    return render_template("index.html")

nowater = 0 
foot = 0
knee = 0
hip = 0    

# poll
@app.route('/poll', methods=["POST","GET"])
def poll():
    level = request.form['level']
#    food = request.form.get('food')
    if level == 'nowater':
        nowater = nowater + 1
    elif level == 'foot':
        foot = foot + 1
    elif level == 'knee':
        knee = knee + 1
    elif level == 'hip':
        hip = hip + 1
    else:
        print ("wrong input******************************************" )   

    foodcol.insert({"level" : level,  "nowater" : nowater, "foot" : foot, "knee" : knee, "hip" : hip }) 
    return render_template("poll.html" )

if __name__ == '__main__':
    app.run(debug=True)        