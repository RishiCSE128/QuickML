from cProfile import label
from email.encoders import encode_7or8bit
from turtle import color
import numpy as np
import pandas as pd
import matplotlib as mpl
mpl.use("TkAgg")
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
def simpleLinearRegression(Xtest, Xtrain, Ytest, Ytrain, dataSet):
    """
    Takes the train and test split of the dataset, as well as name
    of the uploaded dataSet. 
    """
    
    

    regressor = LinearRegression()
    regressor.fit(Xtrain, Ytrain)   

    # plt.rcParams['backend'] = 'GTK3Agg'

    #'GTK3Agg', 'GTK3Cairo', 'GTK4Agg', 'GTK4Cairo', 'MacOSX', 
    # 'nbAgg', 'QtAgg', 'QtCairo', 'Qt5Agg', 'Qt5Cairo', 'TkAgg', 
    # 'TkCairo', 'WebAgg', 'WX', 'WXAgg', 'WXCairo', 
    # 'agg', 'cairo', 'pdf', 'pgf', 'ps', 'svg', 'template'



    plt.title(f'Linear Regression for Dataset: {dataSet}')

    plt.scatter(Xtest[:,:].transpose()[1:,:].tolist()[0], 
                Ytest[:,:].transpose()[1:,:].tolist()[0], 
                color='blue',   
                label='Test Samples')
    
    plt.scatter(Xtrain[:,:].transpose()[1:,:].tolist()[0],
                Ytrain[:,:].transpose()[1:,:].tolist()[0],
                color='red', 
                label = 'Train Samples')
  
    XTest_Plot = Xtest[:,:].transpose()[1:,:].tolist()[0]
    (Ytrain[:,:].transpose()[1:,:].tolist()[0])

    Ytrain_temp = regressor.predict(Xtest) 

    YTrain_Hat_Plot = Ytrain_temp.transpose()[1:,:].tolist()[0]

    print(YTrain_Hat_Plot)

    # print(YTrain_Hat_Plot)

    plt.plot(sorted(XTest_Plot),
             sorted(YTrain_Hat_Plot),
             label='Regression line')

    plt.legend()
    plt.grid()

    filename = f'{random.randint(100,999)}'
    plt.savefig(f'/home/user/Documents/git/QuickML/webapp/static/{filename}.jpg')

    x = f'/home/user/Documents/git/QuickML/webapp/static/{filename}.jpg'

    return x 

