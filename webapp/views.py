import json
from flask import Blueprint, render_template, request, redirect, url_for
import pandas as pd
from sourceCode import Data_Pre_Processing

views = Blueprint('base', __name__)

@views.route('/')
def base(): 
    return render_template('base.html')


@views.route('/', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    dataSet = pd.read_csv(uploaded_file)


    return render_template('home.html', attributes = list(dataSet.columns))
    # if uploaded_file.filename != '':
    #     uploaded_file.save(uploaded_file.filename)
    # 