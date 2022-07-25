### Data Preprocessing Template

## Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

## Importing the dataset
dataset = pd.read_csv('Data.csv')
# Distinguish between Matrix of Features 
X = dataset.iloc[:, :-1].values
# Every row and every column EXCEPT the last - Matrix of Features
# Dependent Variable Vector
Y = dataset.iloc[:, 3]

## Taking Care of Missing Data 
from sklearn.impute import SimpleImputer
# Fitting the Imputer where the missing data resides
# Upper bound exclusive, default mean and 'NaN' arguments 4 Simple Imputer
imputer = SimpleImputer() 
imputer = imputer.fit(X[:,1:3])
X[:,1:3] = imputer.transform(X[:,1:3])

## Encoding Categorical Data 
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
# Encode Country Column
labelencoder_X = LabelEncoder()
X[:,0] = labelencoder_X.fit_transform(X[:,0])
ct = ColumnTransformer([("Country", OneHotEncoder(), [0])], remainder = 'passthrough')
X = ct.fit_transform(X)
labelencoder_Y = LabelEncoder()
Y = labelencoder_Y.fit_transform(Y)

## Splitting the Dataset into Training & Test Set 
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state= 0)

## Feature Scaling 
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)


                              