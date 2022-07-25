import pandas as pd
import numpy as np
import sklearn as sk
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import make_column_transformer 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

var_map = {
    "independent" : ["R&D Spend", "Administration","Marketing Spend", "State"],
    "dependent" : ["Profit"],
    "categorical" : ["State"],
    "missing": ["Marketing Spend"]
}

def dataPreProcess(dataSet, varMap):
    data_root = pd.read_csv(dataSet)
    data = data_root.copy()

    # Splitting Dependent & Independent Variables
    X = data[varMap['independent']]  # DataFrames
    y = data[varMap['dependent']]

    # Removing any missing data
    imputer = SimpleImputer(missing_values=np.nan , strategy='mean')
    imputer = imputer.fit(X[varMap['missing']])
    X[varMap['missing']] =imputer.transform(X[varMap['missing']])

    # Encoding Categorical Variables
    le = LabelEncoder()
    X[varMap['categorical']]= pd.DataFrame(le.fit_transform(X[varMap['categorical']]))
    col_tans = make_column_transformer( 
                         (OneHotEncoder(), 
                         varMap['categorical']))
    Xtemp2 = col_tans.fit_transform(X[varMap['categorical']])
    # Splitting Into Train and Test Set 
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3 , random_state = 0)

    # Feature Scaling
    scale_X = StandardScaler()
    X_train.iloc[: , :] = scale_X.fit_transform(X_train.iloc[: , :])
    X_test.iloc[: , :] = scale_X.fit_transform(X_test.iloc[: , :])

    return(
        {
            'X_train': X_train,
            'X_test': X_test,
            'y_train': y_train,
            'y_test': y_train
        }
    )
    
       
def main():
    response = dataPreProcess('50_Startups.csv', var_map)
    print(response['X_test'])

main()

