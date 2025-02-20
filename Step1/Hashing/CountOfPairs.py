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

# in hashmap key will be element, value will be occurence
index_map = {}
validpairhashingcount = 0
validpairhashing = []
for i, num in enumerate(arr):
    complementary_element = k - arr[i]
    if complementary_element in index_map:
        validpairhashingcount += 1
        validpairhashing.append((i, index_map[complementary_element]))
    else:
        index_map[num] = i
print(validpairhashing)

