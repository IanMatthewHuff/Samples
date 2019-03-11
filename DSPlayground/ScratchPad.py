#%% Imports
import numpy as np
import pandas as pd

#%% Get Our Initial Data
from sklearn import datasets
iris = datasets.load_iris()
X = iris.data[:, [2,3]]
y = iris.target
print('Class labels:', np.unique(y))

#%% Inspect our data
print(iris.DESCR)
iris

#%% Split into test and train data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=1, stratify=y
)
# stratify on y means the same split of propotions of y class labels in test / train

#%% Scale our features first