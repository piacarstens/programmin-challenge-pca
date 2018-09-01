# weather challenge - pia carstens - 1.9.2018
# -------------------------------------------
import numpy as np

# read file 
f = open('weather.csv')

# get data
days  = []
min_T = []
max_T = []

header = f.readline()

for line in f:
    fields =line.split(",")
    days.append(int(fields[0]))
    min_T.append(int(fields[2]))
    max_T.append(int(fields[1]))
    
# get index of smallest temperature difference
dT = list(np.subtract(max_T,min_T))
idx_min_dT = dT.index(min(dT))

print('Day of minimum temperature spread: ', days[idx_min_dT] )