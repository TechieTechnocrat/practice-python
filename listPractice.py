squares = []
for x in range(5):
    squares.append(x**2)
    
# print(squares)

#list comprehension 
trial = [x**3 for x in range(10)]
# print(trial)


courses = ["History", "Maths", "Computer"]
# print(courses[-3])
# print(courses[0])
# print(courses[1:2]) #first index is inclusive but not the second index (basically slicing)
# print(courses[1:]) #goes till last

# courses.append("Spanish")
# courses.insert(1, "Art")
# courses.append("German")

# print(courses)

# courses_2 =["lang", "eng", "french", "german", "spanish"]
# courses.extend(courses_2) #adds each individual item to the list
# courses.append(courses_2) #will append entire list as one item in courses
# print(courses[-1]) #will print entire list courses_2
# print(courses)


popped = courses.pop()

courses.reverse()
courses.sort() #sorts alphabetically
#pass argument reverse=True 
print(courses)

nums = [1, 19, 10, 2, 4, 5]
nums.sort(reverse=True) #ascending order
print(nums)

#now we have sorted function --> if dont want to alter original version
numstrial = [1,5, 2, 4,3]
sorted_nums = sorted(numstrial)
print(sorted_nums)


print(sum(numstrial))

#to find index, index()

print(courses.index('History'))

#to check if its in the lusr
print(courses)
print("Maths" in courses)