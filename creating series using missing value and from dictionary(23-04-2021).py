# creating series using missing value   (23 April)
import numpy as np
import pandas as pd
s1=pd.Series(data=[1,2,np.NaN,'V'])
print(s1)
print(s1.hasnans)
print(s1.head(3))

# creating Series from dictionary
d1={'Jan':31,'Feb':28,'March':31,'April':30,'May':31,'June':30,'July':31,'Aug':31,'Sep':30,'Oct':31,'Nov':30,'Dec':31}
print(d1)
sd=pd.Series(d1)
print(sd)
sd.name='days'
sd.index.name='months'
print(sd) 
