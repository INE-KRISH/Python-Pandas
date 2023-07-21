# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 08:06:41 2021

@author: Admin
"""

import pandas as pd
df=pd.read_csv('C:\\Users\\Admin\\Desktop\\PRACTICAL 2.csv')
df1=pd.DataFrame(df)
print(df1)
print(df1.pivot(index='NAME', columns='FINAL-TERM', values=['CCE1','CCE2']))