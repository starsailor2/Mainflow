import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as datetime
import seaborn as sns

df = pd.read_csv(r"C:\Users\Rishav Raj\Downloads\USvideos.csv")

df.head()
df.describe()
df.info()

df["trending_date"] = df["trending_date"].apply(lambda x : datetime.datetime.strptime(x, '%y.%d.%m'))
df.head(3)

df['publish_time'] = pd.to_datetime(df['publish_time'])
df.head(3)

df['year'] = df['publish_time'].dt.year
yearly_counts = df.groupby('year')['video_id'].count()

#create a bar chart
yearly_counts.plot(kind='bar', xlabel='Year', ylabel='Total Publish Count', title = 'Total publish video per year')

#show the chart
plt.show()

# Group the data by 'category_name' and calculate the sum of 'views' in each category
category_views = df.groupby('category_name')['views'].sum().reset_index()

#sort the categories by views in descending order
top_categories = category_views.sort_values(by='views',ascending=False).head(5)

# create a bar plot to visualize the top 5 categories
plt.bar(top_categories['category_name'], top_categories['views'])
plt.xlabel('Category Name',fontsize=12)
plt.ylabel('Total Views',fontsize=12)
plt.xlabel('Top 5 Categories',fontsize=15)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10,5))
sns.countplot(x='category_name', data=df, order=df['category_name'].value_counts().index)
plt.xticks(rotation=90)
plt.title('Video Count by Category')
plt.show()

videos_per_hour = df['publish_hour'].value_counts().sort_index()

# create a bar plot
plt.figure(figsize=(12,6))
sns.barplot(x=videos_per_hour.index, y=videos_per_hour.values, palette='rocket')
plt.title('Number of Videos Publish per hour')
plt.xlabel('Hour of Day')
plt.ylabel('Number of Videos')
plt.xticks(rotation=45)
plt.show()

#scatter plot between 'views' and 'likes'
sns.scatterplot(data=df, x='views', y='likes')
plt.title('Views Vs Likes')
plt.xlabel('Views')
plt.ylabel('Likes')
plt.show()
