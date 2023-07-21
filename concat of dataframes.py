# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 04:28:11 2021

@author: Admin
"""

import pandas as pd
d1 = {"Calorie":[150,200,300], "duration":[11,10,3]}
x=pd.DataFrame(d1)
print(x.head())
d2= {'Calorie':[120,256,487], 'duration':[50,60,70]}
y=pd.DataFrame(d2)


print(pd.concat([x,y]))

      