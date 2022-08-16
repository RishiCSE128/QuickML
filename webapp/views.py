import os
import json
from tkinter import S
from tabulate import tabulate
from flask import Blueprint, render_template, request, redirect, url_for
import pandas as pd
from sklearn import datasets

from sourceCode import Data_Pre_Processing as DPP

from sourceCode.regression import Simple_Linear_Regression as SLR
from sourceCode.regression import Multiple_Linear_Regression as MLR


# Defining 'views' blueprint. 
# It is registered in webapp/__init__.py
views = Blueprint('base', __name__)

# Constants to be used when user submitted file is stored
UPLOAD_FOLDER = '/home/user/Documents/git/QuickML/sourceCode/'
ALLOWED_EXTENSIONS = {'csv'}

# Making variables writeable by defining it in the global scope. 
filename = ''
name = ''

# Returns base page - starting point of application
@views.route('/')
def base(): 
    return render_template('base.html')


# ================================================================= #

# Invoked when user submits file -  
# creates HTML table with attributes of file
@views.route('/', methods=['POST'])
def upload_file():
    
    global filename
    file = request.files['file']

    # Saves the file so it can be accessed later on.
    dataSet = pd.read_csv(file)
    file.seek(0)
    file.save(os.path.join(UPLOAD_FOLDER, file.filename))
    filename = file.filename

    return render_template('home.html', attributes = list(dataSet.columns))



# ================================================================= #


# Invoked when user submits variable mapping 
@views.route('/dataPreProcessing', methods=['POST'])
def dataPre():
    # result is the variable mapping in a JSON format
    result =  request.get_json()

    # Dataset and variable mapping to be passed into the data
    # pre-processing function - keep a reference to the var map
    varMap = json.loads(result)
    # ddf = pd.DataFrame(varMap)
    # fN_vM = '/home/user/Documents/git/QuickML/pre_processed_data/varMap'
    # ddf.to_csv(fN_vM)

    file = os.path.join(UPLOAD_FOLDER, filename)
    # print(f"The file location is {file}")
    table = DPP.dataPreProcess(file, varMap)

    # Getting the individual components of pre processed data 
    # to keep a reference to them for when they need to be passed 
    # in to the selected algorithm.
    xTest = pd.DataFrame(table['X_test'])
    xTrain = pd.DataFrame(table['X_train'])
    yTest = pd.DataFrame(table['y_test'])
    yTrain = pd.DataFrame(table['y_train'])   

    # Creating variables to store file names and locations for pre 
    # processed data locations
    fN_xT = '/home/user/Documents/git/QuickML/pre_processed_data/xTest'
    fN_xTr = '/home/user/Documents/git/QuickML/pre_processed_data/xTrain'
    fN_yT = '/home/user/Documents/git/QuickML/pre_processed_data/yTest'
    fN_yTr = '/home/user/Documents/git/QuickML/pre_processed_data/yTrain'

    # pd.to_csv creates the file if it does not exist, but it does not 
    # create any non existent directories. The pre_processed_data directory 
    # already exists, pd.to_csv <i>creates</i> the files and populates them 
    # with the contents of their respective components. 
    xTest.to_csv(fN_xT)
    xTrain.to_csv(fN_xTr)
    yTest.to_csv(fN_yT)
    yTrain.to_csv(fN_yTr)

    # Getting the file out of the whole path and converting it to a dataframe.
    name = file.split('/')[-1]
    dF = pd.read_csv(
        os.path.join('/home/user/Documents/git/QuickML/sourceCode', name))
    
    # Columns still hard coded! Fix before deploying to production. 
    col = dF.columns

    # return formattes string which contains HTML and HTML tables using 
    # the 'tabulate' module
    return (f'''
            <h2 style="text-align:center">Scroll to Preview your Pre-Processed Data!</h2>
            <hr>
            <div>
                
                    <h3 style="text-align:left" class="btn btn-primary" data-toggle="collapse"
                     href=".container list"> X train </h3> 
                    <h3 style="text-align:right; margin-top:-40px"> Y train </h3> <hr><br>
                
                <div id="trainset" class="container list" style="display:flex; width=60%">
                    {tabulate(table['X_train'], tablefmt='html', headers = col)}
                    {tabulate(table['y_train'], tablefmt='html', headers = col[4:])}
                </div>
                <hr>
                <h3 style="text-align:left"> X test </h3> 
                <h3 style="text-align:right; margin-top:-40px"> Y test </h3> <hr><br>
                <div class="container" style="display:flex; width=60%">
                    {tabulate(table['X_test'], tablefmt='html', headers = col)}
                    {tabulate(table['y_test'], tablefmt='html', headers = col[4:])}
                </div>
            </div>  
    ''' )

@views.route('/Results', methods=["POST"])
def createModel():
    X_test = pd.read_csv('pre_processed_data/xTest').values
    X_train = pd.read_csv('pre_processed_data/xTrain').values
    Y_test = pd.read_csv('pre_processed_data/yTest').values
    Y_train = pd.read_csv('pre_processed_data/yTrain').values

    os.remove('pre_processed_data/xTest')
    os.remove('pre_processed_data/xTrain')
    os.remove('pre_processed_data/yTest')
    os.remove('pre_processed_data/yTrain')

    os.remove(f'sourceCode/{filename}')

    global name 
    
    with open('choice.txt') as f:
        n = f.read()

    if n == 'ML-REG-SLR':
        name = SLR.simpleLinearRegression(
            X_test, X_train, Y_test, Y_train, filename)     
    elif n == 'ML-REG-MLR':
        name = MLR.multipleLinearRegression(
            X_test, X_train, Y_test, Y_train, filename) 

    return render_template('results.html', x = name)


@views.route('/ProcessOption/<string:option>', methods=['POST'])
def SaveOption(option):
    sel = json.loads(option)

    with open("choice.txt", "w") as fo:
        fo.write(sel)
    return 1

@views.route('/FinalModel')
def showModel():

    os.remove('/home/user/Documents/git/QuickML/choice.txt')

    return render_template(
        'Model_Display.html',
        x = name.split('/')[-1]
    )
