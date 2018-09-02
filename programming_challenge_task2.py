# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 21:36:49 2018

@author: pia carstens
"""
# programming challenge - task 2 - combined weather and football
import numpy as np

# read file 
f = open('football.csv')


# get data
target_value  = []
val1 = []
val2 = []

header = f.readline()

for line in f:
    fields =line.split(",")
    target_value.append(fields[0])
    val1.append(int(fields[5]))
    val2.append(int(fields[6]))
    
# get index of smallest temperature difference
val_diff = list(abs(np.subtract(val1,val2)))
idx_min_val_diff = val_diff.index(min(val_diff))

print('Day of minimum temperature spread: ', target_value[idx_min_val_diff] )
