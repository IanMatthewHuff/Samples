""" Trying out some file basics """

#%%
import numpy as np
import pandas as pd
print('hello world')

#%% Try to just load and see the shape of the data
df = pd.read_csv('SuperHeroes/Data/marvel-wikia-data.csv')
df.head()
