# -*- coding: utf-8 -*-
"""
Created on Sat May 22 16:56:42 2021

@author: Admin
"""


import numpy as np
x=int(input("Enter the number of rows:"))
y=int(input("Enter the number of columns:"))
A1=np.zeros([x,y])
print(A1)
s=0
for r in range (x):
    for c in range (y):
        A1[r,c]=int(input('Enter the data to be entered in array:'))
        s=s+A1[r,c]
print(A1)
print('Sum of all elements of array:',s)
        
        