# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 16:40:26 2021

@author: Admin
"""

import pandas as pd
df={'A':[1,2,3,4,5],'B':[3,4,5,6,7],'C':[5,6,7,8,9],'D':[7,8,9,10,11]}
df1=pd.DataFrame(df,index=['a','b','c','d','e'])
print(df1)
print(df1.quantile(.25, axis = 0))