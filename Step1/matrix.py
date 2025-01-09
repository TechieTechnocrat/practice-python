import numpy as np
# a matrix is columns and rows, a table arrangement 

# how to create a matrix 
# matrix= [[1,2,3], [4,5,6], [7,8,9]]
# print("matrix", matrix)

# #how to take matrix input in python
# # Row = int(input("Enter the number of rows:"))
# # Column = int(input("Enter the number of columns:"))

# # matrix = []
# # print("Enter the entries row wise:")

# # For user input
# # A for loop for row entries
# # for row in range(Row):    
# #     a = []
# #     # A for loop for column entries
# #     for column in range(Column):   
# #         a.append(int(input()))
# #     matrix.append(a)

# # For printing the matrix
# # for row in range(Row):
# #     for column in range(Column):
# #         print(matrix[row][column], end=" ")
# #     print()


# #use list comprehension to create a matrix 
# # matrix_new = [[column for column in range(4)] for row in range(4)]
# # print(matrix_new)

# #using list comprehension to add two matrices
# X = [[1,2,3], [4,5,6], [7,8,9]]
# Y = [[9,8,7],[6,5,4],[3,2,1]]
# result= [[0,0,0],[0,0,0],[0,0,0]]

# #ususally we would do like
# for row in range(len(X)):
#     for col in range(len(X[0])):
#         result[row][col] = X[row][col]+Y[row][col]

# print(result)

# Add_result = [[X[row][col] + Y[row][col] for column in range(len(X[0]))] for row in range(len(X))]
# Subtract_result = [[X[row][col] - Y[row][col] for col in range(len(X[0]))] for row in range(len(X))]


# #matrix multiplication
# for row in range(len(X)):
#     for col in range(len(X[0])):
#         result[row][col] = X[row][col] * Y[row][col]


# for r in result:
#     print(r)


# #matrix division 
# for row in range(len(X)):
#     for col in range(len(X[0])):
#         result[row][col] = X[row][col] // Y[row][col]


# for r in result:
#     print(r)


# #transpose a matrix - make a[i][j] => a[j][i]
# NEW = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

# resultNEW = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# # iterate through rows
# for row in range(len(NEW)):
#     # iterate through columns
#     for column in range(len(NEW[0])):
#         resultNEW[column][row] = NEW[row][column]

# for r in resultNEW:
#     print(r)


# #matrices using numpy 
# x = np.array([[1,2],[4,5]])
# y = np.array([[6,7], [8,9]])

# print(np.add(x, y))
# print(np.subtract(x,y))
# print(np.multiply(x,y))
# print(np.divide(x,y))


Todoarr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
leftsum = 0
rightsum = 0

# Loop through the matrix to calculate diagonal sums
for i in range(len(Todoarr)):
    leftsum += Todoarr[i][i]  # Primary diagonal (left-to-right)
    rightsum += Todoarr[i][len(Todoarr)-i-1]  # Secondary diagonal (right-to-left)

# Calculate and print the absolute difference
result = abs(leftsum - rightsum)
print(result)

