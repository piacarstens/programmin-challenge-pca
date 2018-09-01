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

header = f.readline()

for line in f:
    fields =line.split(",")
    days.append(int(fields[0]))
    min_T.append(int(fields[2]))
    max_T.append(int(fields[1]))
    
print(days)
print(min_T)
print(max_T)
    
