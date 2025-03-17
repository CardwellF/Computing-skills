#name: felix Cardwell
# student number: 2304419

# imports
import random
import matplotlib.pyplot as plt
import numpy as np 

# part 1): change myID value from 111222 to student ID number
myID = "2304419"

# part 2): user imput validation
VarCount = int(input("enter an integer (>=50): "))
is_Valid == True
while is_Valid:
  if VarCount >=50:
    break
  else:
    VarCount = int(input("enter an integer (>=50): "))

# part 3): random seed number
s_d = sum(int(d) for d in myID)
'''
s_d is calculated by adding all the digit in myID together
'''
random.seed(s_d)

# part 4): random list creation
data = [random.randint(1,200) for _ in range(VarCount)]

# calculate sum
data_sum = sum(data)

# calculate mean
data_mean = np.mean(data)

#calculate minimum and maximum
data_min = np.min(data)
data_max = np.max(data)

#print results
print(f"Sum: {data_sum}, Mean: {data_mean:.2f}, Min: {data_min}, Max: {data_max}")

#plot histogram
plt.hist(data, bins=30, alpha=0.6, color="blue")
plt.show()

#code commentary
'''
'''



