# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 10:49:32 2021

@author: Admin
"""
#merging of two dataframe
import pandas as pd
d1 = {"Name":['A','B','C'], "Class":[11,10,3]}
df1=pd.DataFrame(d1)
d2= {'Name':['X','B','Z'], 'Marks':[50,60,70]}
df2=pd.DataFrame(d2)
#inner merge
df3=pd.merge(df1,df2,on='Name',how='inner')
print(df3) 

#outer merge
df3=pd.merge(df1,df2,on='Name',how='outer')
print(df3)

#left merge
df3=pd.merge(df1,df2,on='Name',how='left')   #here first dataframe i.e, df1 is taken
print(df3)                                   # and values of df2 also are taken into
                                             #account
                                             
#right merge
df3=pd.merge(df1,df2,on='Name',how='right')  #here first dataframe i.e, df2 is taken
print(df3)                                   # and values of df1 also are taken into
                                             #account
#concat
print(pd.concat([df1,df2]))

                                             


