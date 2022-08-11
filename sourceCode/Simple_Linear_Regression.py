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

    # print(Xtest[1:,1:].flatten())
    # print(Ytest[1:,1:].flatten())
    # print(Ytrain[1:,1:].flatten())
    # print(Xtrain[1:,1:].flatten())

    # plt.suptitle(f'Linear Regression on {dataset}')



    plt.scatter(Xtest[1:, 1:].flatten(), 
                Ytest[1:, 1:].flatten(), 
                color='blue', label='Test Samples')
    
    plt.scatter(Xtrain[1:, 1:].flatten(),
                Ytrain[1:, 1:].flatten(),
                color='red', 
                label = 'Train Samples')
  
    plt.plot(Xtest[1:, 1:].transpose(), regressor.predict(Xtest)[1:, 1:].flatten(), 'g:', label='Regression line')

    plt.legend()
    plt.grid()

    filename = f'{str(time.time())}_{random.randint(100,999)}'
    plt.savefig(f'/home/user/Documents/git/QuickML/webapp/static/{filename}.jpg')


    return filename