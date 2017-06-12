#import requires libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#import Data
train_df = pd.read_csv("kaggle/titanic-inference/train.csv")
test_df = pd.read_csv("kaggle/titanic-inference/test.csv")

#Defining if being male is and important variable for survival
isMale = train_df["Sex"] == 'male'
males = train_df[isMale]
boolLifeMales = males['Survived']==1
lifeMales = males[boolLifeMales]
count_lifeMales = len(lifeMales['PassengerId'])
count_deadMales = len(males['PassengerId']) - count_lifeMales
print(count_lifeMales)
print(count_deadMales)

isFemale = train_df["Sex"] == 'female'
females = train_df[isFemale]
boolLifeFemales = females['Survived']==1
lifeFemales = females[boolLifeFemales]
count_lifeFemales = len(lifeFemales['PassengerId'])
count_deadFemales = len(females['PassengerId']) - count_lifeFemales
print(count_lifeFemales)
print(count_deadFemales)

#Pie Chart
labels = ['Life Males', 'Life Females', 'Dead Males', 'Dead Females']
sizes = [count_lifeMales, count_lifeFemales, count_deadMales, count_deadFemales]
explode = [0.1,0.1,0.1,0.1]
plt.title('Percentage of dead or alive males or females')
plt.pie(sizes, explode=explode, labels= labels, startangle=90, shadow=True, autopct='%1.1f%%')
"""
#Bar Chart
N = 4
ind = np.arange(N)
plt.bar(ind, sizes, width = 0.8)
"""

plt.show()


