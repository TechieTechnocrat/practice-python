 
arr = [1,1,0,-1,-1]
zeronum = 0
negnum = 0
posnum = 0
for i in range(len(arr)):
    if(arr[i]>0):
        posnum += 1
    elif(arr[i]==0):
        zeronum += 1
    elif(arr[i]<0):
        negnum += 1

posratio = posnum / len(arr)
negratio = negnum / len(arr)
zeroratio = zeronum / len(arr)

print(f"{posratio:.6f}")
print(f"{negratio:.6f}")
print(f"{zeroratio:.6f}")

