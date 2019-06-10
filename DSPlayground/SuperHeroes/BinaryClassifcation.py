''' Classify Super Heroes as either Male or Female '''
#%% Initial Imports
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
%matplotlib inline

#%% Load our dataset first
df = pd.read_csv('SuperHeroes/Data/marvel-wikia-data.csv')
df

#%% Only look at male and female
keep_list = ['Male Characters', 'Female Characters']
df = df[df.SEX.isin(keep_list)]
df


#%% From our dataset drop the columns we don't have
df = df.dropna(subset=['EYE', 'HAIR', 'SEX', 'ALIGN'])
# To make this binary classifications reduce SEX to just Male or Female
df.loc[df.SEX == 'Female Characters', 'BinarySex'] = 0
df.loc[df.SEX == 'Male Characters', 'BinarySex'] = 1
df

#%% Split into test and train data
train, test = train_test_split(df, test_size=0.2)

#%% Start with picking out our feature columns X
feature_columns = ['EYE', 'HAIR', 'ALIGN']
# loc = access rows / columns by lables or boolean array
X = train.loc[:, feature_columns]
X.shape

#%% Then also get our y responses
y = train.BinarySex
y.shape

#%% Convert our text columns to one hot columns

#%% Build scikit-learn model
logreg = LogisticRegression()
logreg.fit(X, y)


#%%
