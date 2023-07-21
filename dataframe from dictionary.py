# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 10:51:36 2021

@author: Admin
"""

import pandas as pd
x={1:'maths', 2:'physics',3:'chemistry',4:'IP',5:'english'}
y={1:100, 2:100,3:100,4:100,5:100}
z={1:'abhay', 2:'vansh',3:'vaidik',4:'arpit',5:'krish'}   

data=pd.DataFrame({'name':z,'subject':x,'marks':y})
print(data)
data.rename(columns={1:'name',2:'subject'})
print(data['name'])