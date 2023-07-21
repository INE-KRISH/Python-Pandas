# -*- coding: utf-8 -*-
"""
Created on Thu May  6 10:45:05 2021

@author: Admin
"""

import pandas as pd
X={'CCE1':[20,20,20,20,20],'CCE2':[22,22,22,22,22]}
Y={'CCE1':[15,16,17,18,19],'CCE2':[12,13,14,15,16]}
df1=pd.DataFrame(X)
df2=pd.DataFrame(Y)
#print(df1)
#print(df2)
print('addition of two dataframe using add:')
print(df1.add(df2))

print('addition of two dataframe using radd:')
print(df1.radd(df2))

print('subtraction of two dataframe using rsub:')
print(df1.rsub(df2))         #here df2-df1 happens rather than df1-df2

print('subtraction of two dataframe using sub:')
print(df1.sub(df2))        #here df1-df2 happens


