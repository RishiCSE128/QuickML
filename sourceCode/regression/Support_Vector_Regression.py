import numpy as np
import pandas as pd
import matplotlib as mpl
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import random

# Using TgAgg backend to make matplotlib thread safe
mpl.use("TkAgg")

import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression    
from sklearn.svm import SVR
    
    
# SUPPORT VECTOR REGRESSION 
def supportVectorRegression(Xtest, Xtrain, Ytest, Ytrain, dataSet):
    
    # Formatting the dataSets for analysis
    XTrain = Xtrain[:,:].transpose()[1:,:].tolist()[0]
    XTest = Xtest[:,:].transpose()[1:,:].tolist()[0]
    YTrain = Ytrain[:,:].transpose()[1:,:].tolist()[0]
    YTest = Ytest[:,:].transpose()[1:,:].tolist()[0]

    # PLR doesn't need a train test split, so the individual components 
    # are combined to form the original dataset (except now its pre-processed)
    X_combined = np.r_[XTrain, XTest]
    Y_combined = np.r_[YTrain, YTest]

    # Manually casting to int becasue row-wise merge 
    # returns floats. 
    X_combined = np.array(X_combined, dtype='int')
    Y_combined = np.array(Y_combined, dtype='int')

    # Creating an SVR regressor
    svr_reg = SVR(kernel='rbf')
    svr_reg.fit(X_combined.reshape(-1,1), Y_combined.reshape(-1,1))

    plt.title(f'Support Vector Regression for {dataSet}')

    # Scattering actual results
    plt.scatter(X_combined, Y_combined, color = 'red', label ='Actual')

    X_combined_Plot = X_combined.tolist()

    # Plotting predicted values via linear regression
    plt.plot(sorted(X_combined_Plot), 
             svr_reg.predict(X_combined.reshape(-1,1)), 
             color = 'blue', 
             label = 'Support Vector')

    plt.legend()          

    filename = f'{random.randint(100,999)}'
    plt.savefig(f'../QuickML/webapp/static/{filename}.jpg')

    x = f'../QuickML/webapp/static/{filename}.jpg'

    return x