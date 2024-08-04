# importimg all the libraries that we need.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

#importing our dataset
df = pd.read_csv('/content/drive/MyDrive/Copy of heart.csv')

df.head()

df.tail()

#take a look at the column names.
df.columns.values

#checking for null values
df.isna().sum()

#concise summary of our dataset
df.info()

#plotting histogram of all numeric values
df.hist(bins = 50, grid= False, figsize=(20,15))

#Generating descriptive statistics.
df.describe()

#plotting histogram of all numeric values
df.hist(bins = 100, grid= True, figsize=(20,15))

questions = ["1. How many people have heart disease and how many people doesn't have heart disease?",
             "2. People of which sex has most heart disease?",
             "3. People of which sex has which type of chest pain most?",
             "4. People with which chest pain are most pron to have heart disease?"]

questions

#Let's find the answer of first question.

#1. How many people have heart disease and how many people doesn't have heart disease?

#getting the values
df.target.value_counts()

#plotting bar chart
df.target.value_counts().plot(kind = 'bar', color = ['red', 'green'])
plt.title("Heart Disease Values")
plt.xlabel("1 = Heart Disease, 0 = No Heart Disease")
plt.ylabel("Amount")

#plotting a pie chart
df.target.value_counts().plot(kind = 'pie', autopct = '%1.1f%%')
plt.title("Heart Disease Values")
plt.ylabel("Count")

# '0' represent 'Female'
# '1' represent 'Male'
# '0' represent 'No disease'
# '1' represent 'Disease'

# Now Let's check how many 'Male' and 'Female' are in the dataset
df.sex.value_counts()

#plotting a pie chart
df.sex.value_counts().plot(kind = 'pie', autopct = '%1.1f%%')
plt.title("Sex Values")
plt.ylabel("Count")
plt.legend(["Female", "Male"])

#Let's find the answer of our 2nd question.

#2. People of which sex has most heart disease?
pd.crosstab(df.sex, df.target)

sns.countplot(x = 'target', hue = 'sex', data = df)
plt.title("Heart Disease frequency for sex")
plt.xlabel("1 = Heart Disease, 0 = No Heart Disease")

#Number of male is more than double in our dataset than female
#More than '45% male' has heart disease and '75% female' has heart disease.

# Let's move to question 3
#3. 'People of which sex has which type of chest pain most ?

# counting values for different chest pain
df.cp.value_counts()

#plotting a bar chart
df.cp.value_counts().plot(kind = 'bar', color = ['red', 'green', 'blue', 'yellow'])
plt.title("Chest Pain type vs count")

pd.crosstab(df.sex, df.cp)

pd.crosstab(df.sex, df.cp).plot(kind = 'bar', figsize = (10,6), color = ['red', 'green', 'blue', 'yellow'])
plt.title("Type of chest pain vs sex")
plt.xlabel("1 = Male, 0 = Female");

#Most of 'male' has 'type 0' chest pain and Least of 'Male' has 'type 4' pain

#in case of 'Female' 'type 0' and 'type 2' percentage is almost same.

#Now question 4!
#4. People with which chest pain are most pron to have heart disease?

pd.crosstab(df.cp, df.target)

sns.countplot(x = 'cp', hue = 'target', data = df)

#Most of people who has 'type 0' chest pain has less chance of heart disease.
#And we see the opposite for other types.
#Now Let's take look at our age column.
#Crete a distribution plot with normal distribution curve

sns.displot(df['age'], bins=30, kde=True)
plt.xlabel("Age")
plt.show()

#From this plot we get a clear overview about maximum heart rate represented by 'thalach'
sns.displot(df['thalach'], bins=30, kde=True, color='chocolate')
plt.xlabel("Age")
plt.show()
