# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 10:46:41 2021

@author: Admin
"""

import pandas as pd
df=pd.read_csv('E:\\ABHAY SINGH\\CLASS 12(all things)\\School class 12\\INFORMATION PRACTICES\\python project\\PANDAS.Data Frame\\PRACTCAL 1.csv')
df1=pd.DataFrame(df)
print(df1)
print(df1.pivot(index='NAME',columns='CLASS',values='SUBJECT'))




