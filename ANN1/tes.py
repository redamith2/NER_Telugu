import os
import pandas as pd
import numpy as np
df1 = pd.read_csv("./data/NER_data.txt",sep="\s+",header=None,dtype=str)
with open("./data/processed2.txt","w+") as file:
    for i in range(df1.shape[0]):
        arr = ""
        if i-2>=0:
            arr = arr + " " + str(df1.iloc[i-2,2])
        else:
            arr = arr + " " + "0"
        if i-1>=0:
            arr = arr + " " + str(df1.iloc[i-1,2])
        else:
            arr = arr + " " + "0"
        arr = arr + " " + str(df1.iloc[i,2])
        if i+1<df1.shape[0]:
            arr = arr + " " + str(df1.iloc[i+1,2])
        else:
            arr = arr + " " + "0"
        if i+2<df1.shape[0]:
            arr = arr + " " + str(df1.iloc[i+2,2])
        else:
            arr = arr + " " + "0"
        file.write(str(df1.iloc[i,1])+" " + arr.strip()+"\n")
