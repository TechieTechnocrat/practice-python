# n = 4
# size = 2*n - 1
# for i in range(1, size):
#     for j in range(1, size):
#         value = max(abs(i - n), abs(j - n)) + 1
#         print(value, end=" ")
#     print()


# print("parrallegoram question")
# n = 4
# for i in range(0, n):
#     for j in range(0, i):
#         print(" ", end="")
#     for j in range(0, n):
#         print("*", end=" ")        
#     print()



print("sum problem")
n = 3
for i in range(1, n+1):
    numbers = "+".join((str(j) for j in range(1, i+1)))
    total = sum(range(1, i + 1))  # Calculate the sum
    print(f"{numbers} = {total}")
