# Count all the (i,j) Pairs such that b[i] + b[j] == k (count of such pairs.) [i<j] 

arr = [1,2,3,4,5]
k = 5
validpair = []
validpaircount = 0

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] + arr[j] == k:
            validpair.append({i , j})
            validpaircount += 1
        
print(validpair, validpaircount)

