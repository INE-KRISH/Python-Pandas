# -*- coding: utf-8 -*-
"""
Created on Thu May  6 11:25:47 2021

@author: Admin
"""

import pandas as pd
x=pd.DataFrame(data=[20,21,24,25,20],columns=['CCE1'])

x['CCE2']=[25,25,25,25,20]

print(x.mode())                #MODE OF A DATAFRAME
print(x['CCE2'].mode())       #MODE OF A DATAFRAME OF A PARTICULAR COLUMN