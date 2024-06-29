import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv(r'C:\Users\Rishav Raj\Downloads\householdtask3.csv')
# show only 10 of the rows
data.head(10)

# scatter/dotted plot with age vs size
plt.scatter(data['age'], data['size'], c="b")

# adding title to that plot
plt.title("Scatter Plot")

# setting the x and y labels
plt.xlabel("age")
plt.ylabel("size")

# show the graph
plt.show()

# Line chart with age against size
plt.plot(data['age']) # x axis
plt.plot(data['size']) # y axis

# adding title to the plot
plt.title("Line chart")

# setting the x and y labels
plt.xlabel("age")
plt.ylabel("size")

# show the graph
plt.show()

# Bar chart or Bar plot
plt.bar(data['age'], data['size'], color="b")

# adding title to the plot
plt.title("Bar chart")

# setting the x and y labels
plt.xlabel("age")
plt.ylabel("size")

# show the graph
plt.show()

# Histogram of own_prop
plt.hist(data['own_prop'])

# set the title for histogram
plt.title("Histogram")

# show the graph
plt.show()



