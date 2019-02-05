''' Here is our first goal view the breakdown of male versus female characters by decade introduced 
'''
#%% Initial imports
import numpy as np
import pandas as pd
print('hello world')

#%% Try to just load and see the shape of the data
df = pd.read_csv('SuperHeroes/Data/marvel-wikia-data.csv')
df.head()


#%% Step One - View all dates
datedf = df[['FIRST APPEARANCE']]
datedf

#%% Step Two - We have NaN columns here, lets drop them
datedf2 = datedf.dropna(subset=['FIRST APPEARANCE'])
datedf2

# #%% Step Three A - Define a function to drop the month
# def reduce_to_year(date_string):
    # return date_string[-2:]

# #%% Step Three B - Apply that function to create a new INTRO YEAR column
# year_added_df = df
# year_added_df['INTRO YEAR'] = year_added_df['FIRST APPEARANCE'].apply(reduce_to_year)
# year_added_df

# Previous idea was not optimal was passing in a pandas series into the reduce_to_year function

#%% Step Three - Add a new INTRO YEAR column
year_added_df = df.dropna(subset=['FIRST APPEARANCE']).copy()
year_added_df['INTRO YEAR'] = year_added_df['FIRST APPEARANCE'][-2:]
year_added_df

#%% Step Three - Add a new INTRO YEAR column, create a copy here as we are going to add a new column
# and we want to keep the previous df clean
year_added_df = df.dropna(subset=['FIRST APPEARANCE']).copy()
year_added_df = year_added_df.assign(intro_year=lambda x: x['FIRST APPEARANCE'][-2:])
year_added_df