arr = [4,4,1,3]
arr.sort()
maxnum = arr[len(arr)-1]
result = 0
for i in range(len(arr)):
    if(arr[i] == maxnum):
        result += 1
    else: 
        result += 0

print(result)


# better code
candles = [3,2,1,3]
maxnum = max(candles)  # Find the maximum height of the candles
resulthi = candles.count(maxnum)  # Count how many candles have the maximum height
print(resulthi)
