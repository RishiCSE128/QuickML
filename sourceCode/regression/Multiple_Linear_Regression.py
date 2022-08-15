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


# MULTIPLE LINEAR REGRESSION 
def multipleLinearRegression(Xtest, Xtrain, Ytest, Ytrain):
    
    return 1 