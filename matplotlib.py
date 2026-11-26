import pandas as pd

data={"Class":["A","B","C","A","B","C"],
      "Score":[85,90,88,72,95,80],
      "Age":[15,16,15,17,16,15],
      
      }
df=pd.DataFrame(data)
print("Original Dataset \n",df)

grouped=df.groupby("Class").mean()
print("Average \n",grouped)
grouped=df.groupby("Class").max()

print("max \n",grouped)
grouped=df.groupby("Class").sum()
print("total \n",grouped)

grouped=df.groupby("Class").min()

print("Minimum \n",grouped)


status=df.groupby("Class").agg({"Score":["mean","min","max"],"Age":["mean","min","max"]}
                  )
print("status \n",status)

"""
grouped=df.groupby("column_name")
for name,group in group:
    print(name)
    print(group)

group.mean()
group.sum()
#aggregation
df.groupby("category_column")["numeric_column"].mean()
df.groupby("category_column").agg({"numeric_column":["mean","max","min"]})
pivot=df.pivot_table(
    values="mumeric_column"
    index="category_column"
    aggfun="mean"
     
)
def range_func(x):
    return x.max()-x.min()

df.groupby("category_column")["numeric_column"].agg(range_func)


df.groupby("category_column")["numeric_column"].mean()
df.groupby("category_column")["numeric_column"].max()
df.groupby("category_column")["numeric_column"].min()

df.groupby("category_column").agg(
    {"numeric_column":["mean","max","min"]})

"""




