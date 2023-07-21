
import pandas as pd
age={'Name':['Abhay','Ajay','Abhinit','Maan','Vansh'],'Age1':[1,2,3,4,5],'Age2':[11,12,13,14,15],'Age3':[21,25,24,36,14]}
df=pd.DataFrame(age,index=['a','b','c','d','e'])
print(df)
#deleting of row
print(df.drop(['a']))
