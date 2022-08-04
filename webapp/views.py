import json
from flask import Blueprint, render_template, request, redirect, url_for
import pandas as pd
from sklearn import datasets
from sourceCode import Data_Pre_Processing as DPP

views = Blueprint('base', __name__)
dataset = None

@views.route('/')
def base(): 
    return render_template('base.html')




@views.route('/', methods=['POST'])
def upload_file():
    file = request.files['file']
    global dataSet
    dataSet = pd.read_csv(file)
    return render_template('home.html', attributes = list(dataSet.columns))





@views.route('/dataPreProcessing', methods=['POST'])
def dataPre():
    result =  request.get_json()
    varMap = json.loads(result)
   
    return DPP.dataPreProcess(dataSet, varMap)
    #return render_template('DPP.html')





    # buliding APIs, data analytics, proficiency in python 
    # python, docker, smart contracts (soliidty)