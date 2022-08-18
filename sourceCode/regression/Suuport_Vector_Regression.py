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

    
    
# SUPPORT VECTOR REGRESSION 
def supportVectorRegression(Xtest, Xtrain, Ytest, Ytrain, dataSet):
    
    

    ## TO DO 



    plt.legend()          

    filename = f'{random.randint(100,999)}'
    plt.savefig(f'../QuickML/webapp/static/{filename}.jpg')

    x = f'../QuickML/webapp/static/{filename}.jpg'

    return x