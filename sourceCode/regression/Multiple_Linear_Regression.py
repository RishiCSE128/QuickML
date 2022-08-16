from cProfile import label
from email.encoders import encode_7or8bit
from turtle import color
import numpy as np
import pandas as pd
import matplotlib as mpl

# Using TgAgg backend to make matplotlib thread safe
mpl.use("TkAgg")

import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import time
import random
from sklearn.metrics import confusion_matrix
import statsmodels as sm 

# MULTIPLE LINEAR REGRESSION 
def multipleLinearRegression(Xtest, Xtrain, Ytest, Ytrain, dataset):
    '''

    '''

    # Fitting Multiple Linear Regression to Training Set 
    regressor = LinearRegression()
    regressor.fit(Xtrain, Ytrain)
    # Test set prediction 
    y_pred = regressor.predict(Xtest)

    # Optimizing Model with Backwards Elimination

    return 1 