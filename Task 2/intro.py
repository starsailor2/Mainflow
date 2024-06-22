import numpy as np
import pandas as pd

# read a csv file from the computer and put it in a dataframe name data
data = pd.read_csv(r"C:\Users\Rishav Raj\Downloads\netflix_titles.csv")

# show the data
print(data)

# Applying the condition in the release year column, only select the movies or tv shows which are release after year 2015.
data.loc[data['release_year'] > 2015].head(5) # head(5) represent to showing the top 5 rows of the data frame juts to get the clarity.

# Modify the column in dataframe by using data.loc and then name of the 
movie = data.loc[data['type'] == 'Movie']
movie

tvseries = data.loc[data['type'] == 'TV Show']
tvseries

data.drop(['show_id','description'], axis=1, inplace=True)
data

data.dropna()
data.describe()
data.shape
data.info()
data.T
