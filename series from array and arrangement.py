import pandas as pd
import numpy as np
x=np.array([1,2,30,25,10,45])
a=pd.Series(x)
print(a)
print(a.sort_values())
