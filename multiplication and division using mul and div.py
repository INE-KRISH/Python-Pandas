# -*- coding: utf-8 -*-
"""
Created on Thu May  6 11:12:02 2021

@author: Admin
"""

import pandas as pd
X={'CCE1':[20,20,20,20,20],'CCE2':[22,22,22,22,22]}
Y={'CCE1':[15,16,17,18,19],'CCE2':[12,13,14,15,16]}
df1 =pd.DataFrame(X)
df2 =pd.DataFrame(Y)
print(df1.mul(df2))        # df1*df2 happens here

print(df1.div(df2))   #df1/df2 happens here
