# -*- coding: utf-8 -*-
"""
Created on Thu May  6 11:14:36 2021

@author: Admin
"""

import pandas as pd
x=pd.DataFrame(data=[20,21,24,25,20],columns=['CCE1'])
print(x)

print('maximum value:',x.max())

print('minimum value',x.min())

print('total:',x.sum())

x['CCE2']=[25,25,25,25,25]
print(x)
print('maximum value:',x.max())

print('maximum value of one column:',x['CCE2'].max())

print('count:',x.count())

print('count of one particular column:',x['CCE1'].count())



