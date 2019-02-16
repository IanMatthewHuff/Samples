''' Here is our first goal view the breakdown of male versus female characters by decade introduced 
'''
#%% Initial imports
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import pandas as pd
%matplotlib inline
print('hello world')

#%% Try to just load and see the shape of the data
df = pd.read_csv('SuperHeroes/Data/marvel-wikia-data.csv')
df.head()

#%% What are the data types of our columns?
print(df.dtypes)

#%% Remove our columns that don't have a year
df = df.dropna(subset=['Year'])
df.head()

#%% Create a decade column to bucket the items
#make_decade = lambda row: (row.Year//10)*10
#col = df.apply(make_decade, axis=1)
#df = df.assign(Decade=col.values)

#%% Better way to do it if we don't get the copy error
df['Decade'] = df.apply(lambda row: (row.Year//10)*10, axis=1)