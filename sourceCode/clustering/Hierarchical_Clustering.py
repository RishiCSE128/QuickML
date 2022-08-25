import numpy as np
import pandas as pd
import matplotlib as mpl

mpl.use("TkAgg")

import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as sch
import random

#Hierarchical Clustering
def hierarchicalClustering(Xtest, Xtrain, Ytest, Ytrain, dataSet):

    # Formatting the dataSets for analysis
    XTrain = Xtrain[:,:].transpose()[1:,:].tolist()[0]
    XTest = Xtest[:,:].transpose()[1:,:].tolist()[0]
    YTrain = Ytrain[:,:].transpose()[1:,:].tolist()[0]
    YTest = Ytest[:,:].transpose()[1:,:].tolist()[0]


    X_combined = np.r_[XTrain, XTest]
    Y_combined = np.r_[YTrain, YTest]

    # Manually casting to int 
    X_combined = np.array(X_combined, dtype='int')
    Y_combined = np.array(Y_combined, dtype='int')

    #Using a Dendrogram to find the optimal number of clusters
    dendrogram = sch.dendrogram(sch.linkage(X_combined.reshape(-1,1), method='ward'))
    # The ward method aims to minimize the variance among the clusters
   
    plt.title(f'Hierarchical Clustering for {dataSet}')
    # plt.xlabel('Number of Clusters')
    plt.ylabel('Euclidean Distances')

    filename = f'{random.randint(100,999)}'
    plt.savefig(f'../QuickML/webapp/static/{filename}.jpg')

    x = f'../QuickML/webapp/static/{filename}.jpg'

    return x 