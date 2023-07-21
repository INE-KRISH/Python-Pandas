# -*- coding: utf-8 -*-
"""
Created on Mon May  3 07:42:22 2021

@author: Admin
"""

import pandas as pd
lis=[{"Vaidik":100,"abhay":100,'vansh':100},{"Vaidik":50,"abhay":50,'vansh':50}]
x=pd.DataFrame(lis,index=['IP','PE'])
print(x)                                    #same key value in the dictionary or it will give error.#
x['Rajvardhan']=[100,99]
print(x)

x['vansh']=[100,51]
print(x)



