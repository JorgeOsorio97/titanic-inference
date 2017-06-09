import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



train_df = pd.read_csv("kaggle/titanic-inference//train.csv")
isMale = train_df["Sex"] == 'male'
males = train_df[isMale]
boolLifeMales = males['Survived']==1
#print(boolLifeMales)
lifeMales = males[boolLifeMales]
count_lifeMales = len(lifeMales['PassengerId'])
#print(lifeMales)

plt.xticks('Men','Women')
plt.bar(2, count_lifeMales)
plt.show()
