# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 23:04:17 2021

@author: Admin
"""

import pandas as pd
data = [['Alex',10],['Bob',12],['Clarke',13]]
df = pd.DataFrame(data,index=['ROW1','ROW2','ROW3'],columns=['Name','marks'])
print (df)


