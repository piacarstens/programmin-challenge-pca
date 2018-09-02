# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 21:36:49 2018

@author: pia carstens
"""
# programming challenge - task 2 - combined weather and football

import numpy as np

def read_data(f,idx_target,idx_val1,idx_val2):
    """ function for reading data for 3 defined indices"""
    target_value  = []
    val1 = []
    val2 = []
    for line in f:
        fields =line.split(",")
        target_value.append(fields[idx_target])
        val1.append(int(fields[idx_val1]))
        val2.append(int(fields[idx_val2]))
    return(target_value,val1,val2)
    

def get_result(target_value,val1,val2):
    """ function for calculating the target_value of the minimum 
    difference of val1 and val2"""
    val_diff = list(abs(np.subtract(val1,val2)))
    idx_min_val_diff = val_diff.index(min(val_diff))
    return target_value[idx_min_val_diff]



# read file 
f = open('football.csv')
header = f.readline()

# assign indices
idx_target = 0
idx_val1 = 5
idx_val2 = 6

# call functions to read data from file and do calculation/get result
(target_value,val1,val2) = read_data(f,idx_target,idx_val1,idx_val2) 
result = get_result(target_value,val1,val2)

# print result
print('Day of minimum temperature spread: ', result )
