import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

#importing our dataset
df = pd.read_csv(r"C:\Users\Rishav Raj\Downloads\disney_plus_titles.csv")

df.head()

df.tail()

#take a look at the column names.
df.columns.values

#checking for null values
df.isna().sum()

#concise summary of our dataset
df.info()

#plotting histogram of all numeric values
df.hist(bins = 50, grid= False, figsize=(10,5))

#plotting histogram of all numeric values
df.hist(bins = 100, grid= True, figsize=(10,5))

#getting the values
df.release_year.value_counts()

#plotting bar chart
df.type.value_counts().plot(kind = 'bar', color = ['red', 'green'])
plt.title("Heart Disease Values")
plt.ylabel("Amount")

# Now Let's check how many 'Movies' and 'TV shows' are in the dataset
df.type.value_counts()

#plotting a pie chart
df.type.value_counts().plot(kind = 'pie', autopct = '%1.1f%%')
plt.title("Types of content")
plt.ylabel("Count")
plt.legend(["Movie", "TV shows"])

# counting values for different list_in
df.listed_in.value_counts()

sns.displot(df['release_year'], bins=30, kde=True)
plt.xlabel("release year")
plt.show()

