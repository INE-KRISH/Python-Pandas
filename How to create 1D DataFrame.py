# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 10:37:03 2021

@author: Admin
"""

import pandas as pd
data = ['Alex','Bob','Clarke','pathin','vansh']
df = pd.DataFrame(data,index=[1,2,3,4,5],columns=['student_NAME'])
print (df)