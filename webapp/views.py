from flask import Blueprint, render_template, request, redirect, url_for
import pandas as pd
from sourceCode import Data_Pre_Processing

views = Blueprint('home', __name__)

@views.route('/')
def home():
    return render_template('base.html')

@views.route('/', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    dataSet = pd.read_csv(uploaded_file)

    print(dataSet.columns)

    return redirect(url_for('home.home'))
    # if uploaded_file.filename != '':
    #     uploaded_file.save(uploaded_file.filename)
    # 