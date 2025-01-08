input_from_user = input()
print(type(input_from_user))


# take multiple inputs
input_string_array = input().split()
print("array" , input_string_array)

#wrong because --> you can not convert the entire list alltogether 
# input_int_array = int(input_string_array)
# print("converted to int", input_int_array)

#right approach - convert one one element 
# input_int_array = [int(element) for element in input_string_array]

input_int_array = []
for element in input_string_array:
    try:
        input_int_array.append(int(element))
    except ValueError:
        print(f"Skipping non-numeric value: {element}")

print("converted to int:", input_int_array)
