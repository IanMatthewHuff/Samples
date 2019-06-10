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

#%% Remove our columns that don't have a year or sex
df = df.dropna(subset=['Year', 'SEX'])
df.head()

#%% Create a decade column to bucket the items
#make_decade = lambda row: (row.Year//10)*10
#col = df.apply(make_decade, axis=1)
#df = df.assign(Decade=col.values)

#%% Better way to do it if we don't get the copy error
df['Decade'] = df.apply(lambda row: (row.Year//10)*10, axis=1)

#%% Show a histogram of heroes by decade
histo_bins = [1930.0, 1940.0, 1950.0, 1960.0, 1970.0, 1980.0, 1990.0, 2000.0, 2010.0, 2020.0]
df.plot.hist(by='Decade', bins=histo_bins, legend=False)

#%% With the bins, do I even need a Decade column?
histo_bins = [1930.0, 1940.0, 1950.0, 1960.0, 1970.0, 1980.0, 1990.0, 2000.0, 2010.0, 2020.0]
df.plot.hist(by='Year', bins=histo_bins, legend=False)

#%% Now see if I can plot the same graph with a difference for gender shown on it
marvel_women_df = df[df.SEX == 'Female Characters']
marvel_men_df = df[df.SEX == 'Male Characters']

plt.hist([marvel_men_df.Year.values, marvel_women_df.Year.values],
    bins=histo_bins, label=['male','female'])
plt.show()
