
from datetime import datetime
#import flask clause from flask package
from flask import Flask

#flask constructor, create a global object
app = Flask (__name__)

#define function to return string
#approute changes to view function
@app.route('/')
def welcome():
    return "Welcome to my Flash Cards App!"

#add new page on url /date
@app.route('/date')
def date():
    return "This page was served at " + str(datetime.now())


counter = 0

@app.route('/count_views')
def count_demo():
    global counter 
    counter += 1
    return "This page was served " + str(counter) + " times"

