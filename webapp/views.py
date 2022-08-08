import os
import json
from tabulate import tabulate
from flask import Blueprint, render_template, request, redirect, url_for
import pandas as pd
from sklearn import datasets
from sourceCode import Data_Pre_Processing as DPP

views = Blueprint('base', __name__)

UPLOAD_FOLDER = '/home/user/Documents/git/QuickML/sourceCode'
ALLOWED_EXTENSIONS = {'csv'}
filename = ''


# Returns base page - starting point of application
@views.route('/')
def base(): 
    return render_template('base.html')

# Invoked when user submits file - 
# creates HTML table with attributes of file
@views.route('/', methods=['POST'])
def upload_file():
    global filename
    file = request.files['file']
    dataSet = pd.read_csv(file)
    file.save(os.path.join(UPLOAD_FOLDER, file.filename))
    filename = file.filename
    return render_template('home.html', attributes = list(dataSet.columns))

# Invoked when user submits variable mapping 
@views.route('/dataPreProcessing', methods=['POST'])
def dataPre():
    result =  request.get_json()

    varMap = json.loads(result)
    file = os.path.join(UPLOAD_FOLDER, filename)

    table = DPP.dataPreProcess(file, varMap)

    return (f'''
            <h2 style="text-align:center">Scroll to Preview your Pre-Processed Data!</h2>
            <hr>
            <div>
                <h3 style="text-align:center"> X train </h3> <hr><br>
                <div class="container" style="display:flex">
                    {tabulate(table['X_train'], tablefmt='html')}
                </div>
                <h3 style="text-align:center"> X test </h3> <hr><br>
                <div class="container" style="display:flex">
                    {tabulate(table['X_test'], tablefmt='html')}
                </div>
                <h3 style="text-align:center"> y train </h3> <hr><br>
                <div class="container" style="display:flex">
                    {tabulate(table['y_train'], tablefmt='html')}
                </div>
                <h3 style="text-align:center"> Y test </h3> <hr><br>
                <div class="container" style="display:flex">
                    {tabulate(table['y_test'], tablefmt='html')}
                </div>
            </div>
    ''' )
    # buliding APIs, data analytics, proficiency in python 
    # python, docker, smart contracts (soliidty)