import pandas as pd


train_df = pd.read_csv("kaggle/titanic/train.csv")
isMale = train_df["Sex"] == 'male'
males = train_df[isMale]
boolLifeMales = males['Survived']==1
print(boolLifeMales)
lifeMales = males[boolLifeMales]
print(lifeMales)
