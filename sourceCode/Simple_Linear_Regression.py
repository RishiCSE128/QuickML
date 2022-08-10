import numpy as np
import pandas as pd
import matplotlib.pyplot as pl
from sklearn.linear_model import LinearRegression

def simpleLinearRegression(Xtest, Xtrain, Ytest, Ytrain):
    
    regressor = LinearRegression()
    regressor.fit(Xtrain, Ytrain)

    y_pred = regressor.predict(Xtest)

    print('size of x = {0}'.format(Xtrain.size))
    print('size of y = {0}'.format(Ytrain.size))
   

    pl.scatter(Xtest.iloc[:, :2], Ytest, color ='red')
    pl.plot(Xtrain.iloc[:, :2], regressor.predict(Xtrain.iloc[:, :2]), color ='blue')

    pl.savefig('/home/user/Documents/git/QuickML/webapp/templates/output.jpg')


   