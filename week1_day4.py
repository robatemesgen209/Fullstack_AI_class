import pandas as pd
import numpy as np

data ={
    "name":["Alice","Bob",np.nan,"boja"],
    "Age":[25,np.nan,30,35],
    "Score":[85,90,np.nan,88]

}
df=pd.DataFrame(data)
print("Original Dataset: \n",df)


df["Age"]=df["Age"].fillna(df["Age"].mean())
df["Score"]=df["Score"].interpolate()
df=df.rename(columns={"Name":"Student_Name","Score":"Exam:Score"})
print("Dataset: \n",df)

df1=pd.DataFrame({
    "ID":[1,2,3],
    "Name":["Alice","Bob","Charlie"],
    "Age":[25,30,35]   

    
})


df2=pd.DataFrame({
    "ID":[1,2,3],
    "Score":[85,90,88]
    })
print("Dataset 1: \n",df1)
print("Dataset 2: \n", df2)




