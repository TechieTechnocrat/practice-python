alicearr = [1, 2, 3]
bobarr = [3, 2, 1]
alice = 0
bob = 0

result =[]

for i in range(len(alicearr)):
    if alicearr[i] > bobarr[i]:
        alice += 1

    elif alicearr[i] < bobarr[i]:
        bob += 1

result.append(alice)
result.append(bob)

print("Alice's score:", result )

