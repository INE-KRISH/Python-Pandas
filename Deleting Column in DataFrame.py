import pandas as pd
age={'Name':['Abhay','Ajay','Abhinit','Maan','Vansh'],'Age1':[1,2,3,4,5],'Age2':[11,12,13,14,15],'Age3':[21,25,24,36,14]}
df=pd.DataFrame(age)
print(df)
# Age in 2025
df['Age in 25']=df['Age1']+24
print(df)
# Addition of Ages
df['Total Age']=df['Age1']+df['Age2']+df['Age3']
print(df)

print(df.iloc[2:0:-1,1:4])
print(df['Age1'])

# deleting column
df2=df.drop('Age1',axis=1)
print(df2)
del df['Age3']
print(df)