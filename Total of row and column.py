# -*- coding: utf-8 -*-
"""
Created on Mon May  3 10:17:13 2021

@author: Admin
"""

import pandas as pd
lis=[{"Vaidik":100,"abhay":100,'vansh':100},{"Vaidik":50,"abhay":50,'vansh':50}]
x=pd.DataFrame(lis,index=['IP','PE'])
print(x[1:2])                                    #same key value in the dictionary or it will give error.
#x['total']=x["Vaidik"]+x["abhay"]+x['vansh']
#print(x)
print(x.sum("Vaidik"),axis=1)


