#lets implement chaining in python

# class myHashTable:
#     def __init__(self):
#         self.MAX = 10
#         self.arr = [None for i in range(self.MAX)]

#     def get_hash(self, key):
#         hash = 0
#         for char in key:
#             hash += ord(char)
#         return hash % self.MAX
#     def __getitem__(self, index):
#         h = self.get_hash(index)
#         return self.arr[h]
#     def __setitem__(self, key, val):
#         h = self.get_hash(key)
#         self.arr[h] = val
    

#now march 17 overwritten the value for march 6
#so when we print we will get 20 instead of 120


#now lets make modifications 
#instead of strong none we will store []
# Inserts or updates a key-value pair: 
# __setItem__ if key already exists --> 
# update the value, if not append the new key - 
# value pair to handle collision


class myHashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX

    def __getitem__(self, index):
        h = self.get_hash(index)
        for element in self.arr[h]:
            if element[0] == index:
                return element[1]
            

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False  # Initialize the 'found' variable
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, val)
                found = True
                break
        if not found:
            self.arr[h].append((key, val))
    def _deleteitem__(self, key):
        h = self.get_hash(key)


# Testing the hash table
t = myHashTable()
t["march 6"] = 120
t["march 6"] = 1120
t["march 8"] = 110
t["march 9"] = 100
t["march 17"] = 20
t["march 18"] = 10

print(t.arr)
print(t["march 17"])


# Collision Handling:
# If multiple key-value pairs exist at the same index (chaining), the code checks if the key already exists.
# If it exists, the value is updated.
# Otherwise, the new key-value pair is appended to the list at that index.


# Example of updation:

# self.arr = [
#     [], 
#     [], 
#     [("cat", 10), ("bat", 20)],  # Index 2 has two key-value pairs
#     [], 
#     []
# ]
# h = 2  # Hash index
# key = "cat"
# val = 50
# found = False
# Execution:
# for idx, element in enumerate(self.arr[h]):

# Loop starts with self.arr[2] → [("cat", 10), ("bat", 20)].
# idx = 0, element = ("cat", 10).
# if len(element) == 2 and element[0] == key:

# Checks:
# len(element) == 2 → True (it's a key-value pair).
# element[0] == key → True ("cat" == "cat").
# self.arr[h][idx] = (key, val)

# Updates the value for "cat":
# css
# Copy code
# self.arr[2] → [("cat", 50), ("bat", 20)]
# found = True

# Marks that the key has been updated.
# break

# Exits the loop since the key has been updated.