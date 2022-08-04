import pandas as pd
import json as j
import numpy as np
import sklearn as sk
from csv import reader
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import make_column_transformer 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def dataPreProcess(dataSet, varMap):
    data = pd.DataFrame(dataSet)

    # Splitting Dependent & Independent Variables
    X = data[varMap['Independent']]  # DataFrames
    y = data[varMap['Dependent']]

    # # Removing any missing data
    # imputer = SimpleImputer(missing_values=np.nan , strategy='mean')
    # imputer = imputer.fit(X[varMap['Missing']])
    # X[varMap['Missing']] =imputer.transform(X[varMap['Missing']])

    # Encoding Categorical Variables
    le = LabelEncoder()
    X[varMap['Categorical']]= pd.DataFrame(le.fit_transform(X[varMap['Categorical']]))
    col_tans = make_column_transformer( 
                         (OneHotEncoder(), 
                         varMap['Categorical']))
    Xtemp2 = col_tans.fit_transform(X[varMap['Categorical']])
    
    # Splitting Into Train and Test Set 
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3 , random_state = 0)

    # Feature Scaling
    scale_X = StandardScaler()
    X_train.iloc[: , :] = scale_X.fit_transform(X_train.iloc[: , :])
    X_test.iloc[: , :] = scale_X.fit_transform(X_test.iloc[: , :])

    # Returns a dictionary of preprocessed data
    return(
        {
            'X_train': X_train,
            'X_test': X_test,
            'y_train': y_train,
            'y_test': y_test
        }
    )
    
       
# def main():
#     file = '~/Documents/git/QuickML/50_Startups.csv'
#     response = dataPreProcess(file, var_map)
#     print(response['X_test'])

# main()

