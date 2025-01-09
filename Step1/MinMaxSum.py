import numpy as np 
arr = [3,5,1,9,7]
minsum = 0
maxsum = 0
 

# logic 
# The minimum sum will be the sum of all integers except the largest one.
# The maximum sum will be the sum of all integers except the smallest one.


arr.sort()
print(arr)

minsum = sum(arr[:4])
maxsum = sum(arr[1:])
    
print(minsum, maxsum)