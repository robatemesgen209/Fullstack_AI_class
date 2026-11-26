import pandas as pd
url="https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df=pd.read_csv(url)
print(df.info())
print(df.describe())


df["Age"]=df["Age"].fillna(df["Age"].median())
df["Embarked"]=df["Embarked"].fillna(df["Embarked"].mode()[0])
df=df.drop_duplicates()
first_class=df[df["Pclass"]==1]
print("First Class Passenger: \n",first_class.head())