import numpy as np
import pandas as pd
df=pd.read_csv('iris.csv',header=0)#,usecols='sepal.length,sepal.width'
print(df[["sepal.length","variety"]])
p=df.loc[df["variety"]=="Setosa"]
print(p)
