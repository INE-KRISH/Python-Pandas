# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 11:16:50 2021

@author: Admin
"""

import pandas as pd
data = [['Alex',10],['Bob',15],['Clarke',13]]
df = pd.DataFrame(data,index=['ROW1','ROW2','ROW3'],columns=['Name','marks'])
print (df)
print(df.sort_values(by='marks',ascending=True))
df['class']=[10,9,8]
df['stream']=['s','c','s']
print(df)
df3=df.rename(columns={'marks':'%age'})
print(df3)

df4=df.loc('marks')
print(df4)

print(df.iloc[2:0:-1,1:4])
      
df2=df.drop('marks',axis=1)
print(df2)

