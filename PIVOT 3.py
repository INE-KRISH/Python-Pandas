# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 11:16:38 2021

@author: Admin
"""

import pandas as pd
x={'item':['TV','TV','AC','AC'],'Company':['LG','VIDEOCON','LG','SONY'],'RUPEE':[10000,12000
                                                                                 ,15000,14000],'USD':[700,650,800,750]}
df=pd.DataFrame(x)
print(df)
print(df.pivot(index='item',columns='Company',values='USD'))