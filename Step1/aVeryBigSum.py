# in python, value of an integer is not restricted by the number of bits
# it can expand to the limit of available memory 

sum_given = [10000000000000000000000000000000000000000000, 10000000000000000000000000000000000000000000, 1000*100]
sum = 0
for x in sum_given:
    sum += x
print(sum)

#python handles it automatically

x = 10
print(type(x)) 
  
x = 10000000000000000000000000000000000000000000
print(type(x))  #python 2.7 will give it type long byt python 3 only has int