# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 11:37:26 2021

@author: Admin
"""

import pandas as pd

df = pd.DataFrame([[1, 2], [4, 5], [7, 8]],
     index=['cobra', 'viper', 'sidewinder'],
     columns=['max_speed', 'shield'])
print(df)

df.loc['Black Mamba']=[20,5]
print(df)