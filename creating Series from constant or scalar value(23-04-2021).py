# creating Series from constant/scalar value  (23 April)
import pandas as pd
s1=pd.Series(data='Informatics Practices',index=[1,2,3,4,5,6,7])
print(s1)

s2=pd.Series(data='Class12',index=['a','b','c','d'])
print(s2)

s3=pd.Series(data='Class12',index=[x for x in 'abcd'] )
print(s3)

