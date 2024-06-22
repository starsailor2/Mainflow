import numpy as np
import pandas as pd

# read a csv file from the computer and put it in a dataframe name data
data = pd.read_csv(r"C:\Users\Rishav Raj\Downloads\netflix_titles.csv")

# show the first 10 data from the dataframe
print(data.head(10))

# Applying the condition in the release year column, only select the movies or tv shows which are release after year 2015.
print(data.loc[data['release_year'] > 2015].head(5)) # head(5) represent to showing the top 5 rows of the data frame juts to get the clarity.

# select the rows which is showing 'type' column a "movie" in dataframe that means to satisfies the given condition inside .loc  
movie = data.loc[data['type'] == 'Movie']
print(movie)


# select the rows which is showing 'type' column a "TV show" in dataframe that means to satisfies the given condition inside .loc 
tvseries = data.loc[data['type'] == 'TV Show']
print(tvseries)

# To delete a particular row or column by using axis (1 for column & 0 for the row), we use .drop and select the particular 
data.drop(['show_id','description'], axis=1, inplace=True)
print(data)

# To drop the whole rows which contain even a single NaN or NaT, we use ".dropna" 
print(data.dropna()) 

# it gives the statistical analysis of the data sets like (mean, count, std, min) and so on....
print(data.describe())

# it gives us the matrix rows and column in the format (r X c)
print(data.shape)

# it is use to make a transpose of a matrix
print(data.T)
