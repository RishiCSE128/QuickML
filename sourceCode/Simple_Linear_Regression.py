from cProfile import label
from turtle import color
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import time
import random

def simpleLinearRegression(Xtest, Xtrain, Ytest, Ytrain):
    
    regressor = LinearRegression()
    regressor.fit(Xtrain, Ytrain)   

    Xtest[:,1:].tolist().sort()
    Ytest[:,1:].tolist().sort()
    Xtrain[:,1:].tolist().sort()
    Ytrain[:,1:].tolist().sort()
 
    plt.scatter(Xtest[:,:].transpose()[1:,:].tolist()[0], 
                Ytest[:,:].transpose()[1:,:].tolist()[0], 
                color='blue',   
                label='Test Samples')
    
    plt.scatter(Xtrain[:,:].transpose()[1:,:].tolist()[0],
                Ytrain[:,:].transpose()[1:,:].tolist()[0],
                color='red', 
                label = 'Train Samples')
  
    plt.plot(Xtest[:,:].transpose()[1:,:].tolist()[0], 
             regressor.predict(Xtest), 
             label='Regression line')


    # plt.plot(Xtest[:,:].transpose()[1:,:].tolist()[0],
    #          regressor.predict(Xtest)[:,:].transpose()[1:,:].tolist()[0], 
    #          label='Regression line')
    #'g:'#

    plt.legend()
    plt.grid()

    filename = f'{str(time.time())}_{random.randint(100,999)}'
    plt.savefig(f'/home/vladi/Documents/git/QuickML/webapp/static/{filename}.jpg')

    return filename