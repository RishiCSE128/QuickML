from cProfile import label
from email.encoders import encode_7or8bit
from turtle import color
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import time
import random
from sklearn.metrics import confusion_matrix
import io
import base64


def fig_to_base64(fig):
    img = io.BytesIO()
    fig.savefig(img, format='png',
                bbox_inches='tight')
    img.seek(0)

    return base64.b64encode(img.getvalue())

# SIMPLE LINEAR REGRESSION
def simpleLinearRegression(Xtest, Xtrain, Ytest, Ytrain):
    
    regressor = LinearRegression()
    regressor.fit(Xtrain, Ytrain)   

    Xtest[:,1:].tolist().sort()
    Ytest[:,1:].tolist().sort()
    Xtrain[:,1:].tolist().sort()
    Ytrain[:,1:].tolist().sort()
 
    fig = plt.figure()

    plt.scatter(Xtest[:,:].transpose()[1:,:].tolist()[0], 
                Ytest[:,:].transpose()[1:,:].tolist()[0], 
                color='blue',   
                label='Test Samples')
    
    plt.scatter(Xtrain[:,:].transpose()[1:,:].tolist()[0],
                Ytrain[:,:].transpose()[1:,:].tolist()[0],
                color='red', 
                label = 'Train Samples')
  
    plt.plot(Xtest[:,:].transpose()[1:,:].tolist()[0],
             regressor.predict(Xtest)[:,:].transpose()[1:,:].tolist()[0], 
             label='Regression line')
    #'g:'#

    plt.legend()
    plt.grid()

    filename = f'{random.randint(100,999)}'
    plt.savefig(f'/home/vladi/Documents/git/QuickML/webapp/static/{filename}.png')

    encoded = fig_to_base64(fig)

    my_html = '<img src="data:image/png;charset=utf-8;base64, {}">'.format(encoded.decode('utf-8'))

    return encoded

# MULTIPLE LINEAR REGRESSION 
