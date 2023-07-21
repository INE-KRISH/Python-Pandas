# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 19:38:28 2021

@author: Admin
"""

import pandas as pd
x={'NAME':['Abhay','Aditya','Aman','Abhinav','Daivik'], 'ROLL_NO.':[1,2,3,4,5], '%age':[100,100,100,100,100]}
df1=pd.DataFrame(x,index=['a','b','c','d','e'])
print(df1)
print(df1.reindex(['a1','a2','a3','a4','a5'],copy=True))


#fill_value is used to fill all the values of NaN 
