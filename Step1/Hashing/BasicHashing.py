# first step of implementing hashing in python is writing its hash function 
 
# def get_hash_function(key):
#     h = 0 
#     for char in key : 
#         h+= ord(char) 
#     return h % 100


#here we know ord('a') we get its ASCII value
# calculated the sum of ascii values of all the characters character in it
# array size is 100, calculated its index by MOD(value, sizeofarray)


# to implement hashtable, create a class in python 
class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)] #used list comprehension here
    def get_hash(self, key):
        h = 0
        for char in key:
            h+=ord(char)
        return h % self.MAX
    def add(self, key, val): #__getitem__
        h = self.get_hash(key)
        self.arr[h] = val
    def get(self, key):
        h = self.get_hash(key) #__setItem__
        return self.arr[h]


#now create an object 
t = HashTable()
t.get_hash('march 6')
t.add('march 9', '676746')
t.add('march 4', '676746')
print(t.get('march 4'))

print(t.arr)