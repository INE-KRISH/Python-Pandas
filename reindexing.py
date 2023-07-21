import pandas as pd
import numpy as np
x=np.array([1,2,30,25,10,45])
a=pd.Series(x,index=['A','B','C','D','E','F'])
print(a)
a.index=(1,2,3,4,5,6)
print(a)
