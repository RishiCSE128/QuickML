from cProfile import label
from turtle import color
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import time
import random

def simpleLinearRegression(Xtest, Xtrain, Ytest, Ytrain, dataset='Salary data'):
    
    regressor = LinearRegression()
    regressor.fit(Xtrain, Ytrain)   

    plt.suptitle(f'Linear Regression on {dataset}')
    plt.scatter(Xtest, Ytest, color='blue', label='Test Samples')
    plt.scatter(Xtrain,Ytrain,color='red', label = 'Train Samples')

    plt.plot(Xtest, regressor.predict(Xtest), color ='green', label='Regression line')

    plt.legend()
    plt.grid()

    filename = f'{str(time.time())}_{random.randint(100,999)}'
    plt.savefig(f'/home/user/Documents/git/QuickML/webapp/static/{filename}.jpg')


    return filename