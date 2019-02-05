""" Trying out some file basics """

#%%
import numpy as np
import pandas as pd

print('hello world')

#%% 
pd.read_csv("Books/test.csv")

#%% Try to load a single book and divide it up by spaces
pd.read_csv('Books/Content/Alice.txt', delim_whitespace=True)

