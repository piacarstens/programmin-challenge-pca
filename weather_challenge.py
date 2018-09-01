# weather challenge - pia carstens - 1.9.2018
# -------------------------------------------

# read file
f=open('weather.csv')
#file = f.read()
#print(file)

# get data
days  = []
min_T = []
max_T = []

for line in f:
    fields =line.split(",")
    days.append(fields[0])
    min_T.append(fields[1])
    max_T.append(fields[2])
    
print(days)
print(min_T)
print(max_T)