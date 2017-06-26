#import requires libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#import Data
train_df = pd.read_csv("kaggle/titanic-inference/train.csv")
test_df = pd.read_csv("kaggle/titanic-inference/test.csv")

#Drop unecesarry data for the mechine learnig purpose

train_df = train_df.drop(['Name', 'Ticket', 'Embarked'], axis=1)
test_df = test_df.drop(['Name', 'Ticket', 'Embarked'], axis=1)
#Defining if being male is an important variable for survival
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
plt.title('Percentage of dead or alive males and females')
plt.pie(sizes, explode=explode, labels= labels, startangle=90, shadow=True, autopct='%1.1f%%')
"""
#Bar Chart
N = 4
ind = np.arange(N)
plt.bar(ind, sizes, width = 0.8)
"""

plt.show()

print('Being a male is an important factor as such must of males died')


#Defining if being in a higher class is an important variable for survival

class_3 = train_df[train_df['Pclass']==3]
class_2 = train_df[train_df['Pclass']==2]
class_1 = train_df[train_df['Pclass']==1]
lifeClass_3 = class_3[class_3['Survived']==1]
lifeClass_2 = class_2[class_2['Survived']==1]
lifeClass_1 = class_1[class_1['Survived']==1]
